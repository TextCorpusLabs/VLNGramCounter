import pathlib
import typing as t

def list_folder_documents(folder_in: pathlib.Path) -> t.Iterator[pathlib.Path]:
    """
    Lists the documents in the folder

    Parameters
    ----------
    folder_in : pathlib.Path
        The folder path containing all the documents
    """
    def _is_txt_document(file_path: pathlib.Path) -> bool:
        result = \
            file_path.is_file() and \
            file_path.suffix.lower() == '.txt' and \
            not file_path.stem.startswith('_')
        return result
    for file_name in folder_in.iterdir():
        if file_name.is_file():
            if _is_txt_document(file_name):
                yield file_name

