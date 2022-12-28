import pathlib
import progressbar as pb
import typing as t
from ... import common_types as ct

T = t.TypeVar('T')

def guess_encoding(file_name: pathlib.Path) -> str:
    """
    Guess the encoding of a file

    Parameters
    ----------
    file_name : pathlib.Path
        The file at issue
    """
    with open(file_name, 'rb') as fp:
        b = fp.read(2)
    if ((len(b) >= 2) and ((b[0:2] == b'\xfe\xff') or (b[0:2] == b'\xff\xfe'))):
        return "utf-16"
    else:
        return "utf-8"

def list_jsonl_documents(jsonl_in: pathlib.Path) -> t.Iterator[ct.Document]:
    """
    Lists the documents in the `JSONL` file

    Parameters
    ----------
    jsonl_in : pathlib.Path
        The JSONL containing all the documents
    """
    encoding = guess_encoding(jsonl_in)
    with open(jsonl_in, 'r', encoding = encoding) as fp:
        with jl.Reader(fp) as reader:
            for item in reader:
                yield item

def list_folder_documents(folder_in: pathlib.Path, is_document: t.Callable[[pathlib.Path], bool]) -> t.Iterator[str]:
    """
    Lists the documents in the folder

    Parameters
    ----------
    folder_in : pathlib.Path
        The folder path containing all the documents
    """
    for file_name in folder_in.iterdir():
        if is_document(file_name):
            yield str(file_name)

def list_merged_folder_documents(folders_in: t.List[pathlib.Path], is_document: t.Callable[[pathlib.Path], bool]) -> t.Iterator[t.List[str]]:
    """
    Lists the documents in the merge folders

    Parameters
    ----------
    folders_in : pathlib.Path
        The folders containing the documents to merge 
    """
    for i in range(len(folders_in)):
        folder = folders_in[i]
        for file_name in folder.iterdir():
            if is_document(file_name):
                result = [f.joinpath(file_name.name) for f in folders_in]
                exists = [f.exists() for f in result]
                if i > 0 and any(exists[0:i]):
                    continue
                docs = [str(result[i]) for i in range(len(result)) if exists[i]]
                yield docs


def is_txt_document(file_path: pathlib.Path) -> bool:
    """
    Determines if the file should be included in the processing
    """
    result = \
        file_path.is_file() and \
        file_path.suffix.lower() == '.txt' and \
        not file_path.stem.startswith('_')
    return result



def progress_overlay(items: t.Iterator[T], title: str) -> t.Iterator[T]:
    bar_i = 0
    widgets = [title, ' ', pb.Counter(), ' ', pb.Timer(), ' ', pb.BouncingBar(marker = '.', left = '[', right = ']')]
    with pb.ProgressBar(widgets = widgets) as bar:
        for item in items:
            bar_i = bar_i + 1
            bar.update(bar_i)
            yield item
