import pathlib

def folder(text: str) -> pathlib.Path:
    path = pathlib.Path(text)
    if not path.exists():
        raise ValueError(f'{str(text)} is does not exist')
    if not path.is_dir():
        raise ValueError(f'{str(text)} is not a folder')       
    return path

def file(text: str) -> pathlib.Path:
    path = pathlib.Path(text)
    if not path.exists():
        raise ValueError(f'{str(text)} is does not exist')
    if not path.is_file():
        raise ValueError(f'{str(text)} is not a folder')       
    return path

def nonzero_int(text: str) -> int:
    val = int(text)
    return val
