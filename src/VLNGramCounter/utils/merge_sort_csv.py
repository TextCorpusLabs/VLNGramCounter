import csv
import multiprocessing as mp
import pathlib
import progressbar as pb # type: ignore
import typing as t
from uuid import uuid4

class _merge_arg:
    def __init__(self, file_1: pathlib.Path, file_2: pathlib.Path, cache_dir: pathlib.Path):
        self.file_1 = file_1
        self.file_2 = file_2
        self.cache_dir = cache_dir

def merge_sort_csv(file_paths: t.List[pathlib.Path], cache_dir: pathlib.Path) -> pathlib.Path:
    widgets = ['Merges Left ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
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
    readers = [_read_csv_file(args.file_1), _read_csv_file(args.file_2)]
    current = [next(readers[0]), next(readers[1])]
    cnt = len(current)
    with open(file_name, 'w', encoding = 'utf-8', newline = '') as fp:
        writer = csv.writer(fp, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
        while cnt > 0:
            i = _min_index(current)
            writer.writerow(current[i])
            current[i] = next(readers[i], None) # type: ignore
            if current[i] is None:
                cnt = cnt - 1
    return file_name

def _read_csv_file(file_path: pathlib.Path) -> t.Iterator[t.List[str]]:
    with open(file_path, 'r', encoding = 'utf-8') as fp:
        reader = csv.reader(fp, delimiter = ',', quotechar = '"')
        for item in reader:
            yield item
    file_path.unlink()

def _min_index(lines: t.List[t.List[str]]) -> int:
    len_ngs = len(lines)
    min_i: int = 0
    min_ng: str = ''
    for i in range(len_ngs):
        if lines[i] is not None:
            min_ng = lines[i][0]
            min_i = i
            break
    for i in range(min_i + 1, len_ngs):
        curr = lines[i][0]
        if curr is not None and curr < min_ng:
            min_ng = curr
            min_i = i
    return min_i
