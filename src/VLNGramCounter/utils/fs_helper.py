import csv
import pathlib
import typing as t
from ..dtypes import trie
from uuid import uuid4

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

def read_lines_in_files(source_files: t.Iterator[pathlib.Path]) -> t.Iterator[str]:
    """
    Reads all the lines in all the files as an `Iterator`

    Parameters
    ----------
    file_path : pathlib.Path
        The file to read
    """
    def _read_lines_in_file(file_path: pathlib.Path) -> t.Iterator[str]:
        with open(file_path, 'r', encoding = 'utf-8') as fp:
            for line in fp:
                yield line
    for file in source_files:
        for line in _read_lines_in_file(file):
            yield line

def write_ngram_chunks(chunks: t.Iterator[trie], cache_dir: pathlib.Path) -> t.Iterator[pathlib.Path]:
    """
    Writes all the ngrams in all the chunks as an `Iterator`

    Parameters
    ----------
    chunks : Iterator[trie]
        The chunks to process
    cache_dir: pathlib.Path
        The path to save chunks
    """
    def _write_ngram_chunk(chunk: trie, cache_dir: pathlib.Path) ->  pathlib.Path:
        file_name = cache_dir.joinpath(f'tmp_{uuid4()}.csv')
        with open(file_name, 'w', encoding = 'utf-8', newline = '') as fp:
            writer = csv.writer(fp, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)
            for ngram in chunk.enumerate():
                writer.writerow([curr.gram, curr.count])
        return file_name
    for chunk in chunks:
        yield _write_ngram_chunk(chunk, cache_dir)
