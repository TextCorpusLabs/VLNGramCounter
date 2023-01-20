import multiprocessing as mp
import pathlib
import progressbar as pb # type: ignore
import typing as t
from uuid import uuid4
from .fs_helper import read_ngram_chunk

class _merge_arg:
    def __init__(self, file_1: pathlib.Path, file_2: pathlib.Path, cache_dir: pathlib.Path):
        self.file_1 = file_1
        self.file_2 = file_2
        self.cache_dir = cache_dir

def merge_sort_chunks(file_paths: t.List[pathlib.Path], cache_dir: pathlib.Path) -> pathlib.Path:
    widgets = ['Merging ', pb.Counter(), ' Files ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets, initial_value = len(file_paths)) as bar:
        with mp.Pool() as pool:
            bar.update(len(file_paths), force = True) # type: ignore
            while len(file_paths) > 1:
                pairs = (pair for pair in _pair_files(file_paths))
                args = (_merge_arg(p[0], p[1], cache_dir) for p in pairs)
                args = list(args)
                file_paths = list(pool.imap_unordered(_merge_files, args))
                bar.update(len(file_paths)) # type: ignore
    return file_paths[0]

def _pair_files(file_paths: t.List[pathlib.Path]) -> t.Iterator[t.List[pathlib.Path]]:
    t1: pathlib.Path | None = None
    for file_path in file_paths:
        if t1 is None:
            t1 = file_path
        else:
            yield [t1, file_path]
            t1 = None
    if t1 is not None:
        yield [t1, None] # type: ignore

def _merge_files(args: _merge_arg) -> pathlib.Path:
    if args.file_2 is None:
        return args.file_1
    file_name = args.cache_dir.joinpath(f'tmp_{uuid4()}.csv')
    readers = [read_ngram_chunk(args.file_1), read_ngram_chunk(args.file_2)]
    current = [next(readers[0]), next(readers[1])]
    cnt = len(current)
    with open(file_name, 'w', encoding = 'utf-8', newline = '') as fp:
        while cnt > 0:
            i = _min_index(current)
            fp.write(f'{current[i][0]},{current[i][1]}\n')
            current[i] = next(readers[i], None) # type: ignore
            if current[i] is None:
                cnt = cnt - 1
    args.file_1.unlink()
    args.file_2.unlink()
    return file_name

def _min_index(lines: t.List[t.List[str]]) -> int:
    len_ngs = len(lines)
    min_i: int = 0
    min_ng: str = ''
    for i in range(len_ngs):
        if lines[i] is not None:
            min_ng = lines[i][1]
            min_i = i
            break
    for i in range(min_i + 1, len_ngs):
        if lines[i] is not None:
            curr = lines[i][1]
            if curr < min_ng:
                min_ng = curr
                min_i = i
    return min_i
