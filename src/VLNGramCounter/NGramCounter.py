import pathlib
import shutil
import typing as t
from . import utils
from .dtypes import settings, trie

class NGramCounter:

    def __init__(self, settings: settings):
        """
        Counts large corpuses of ngrams

        Parameters
        ----------
        settings : dtypes.settings
            The settings for the counter
        """
        self._settings = settings
        self._include: trie = None # type: ignore
        self._exclude: trie = None # type: ignore

    def init(self) -> None:
        self._settings.validate()
        if self._settings.dest.exists():
            self._settings.dest.unlink()
        if self._settings.cache_dir.exists():
            shutil.rmtree(self._settings.cache_dir)
        self._settings.cache_dir.mkdir(parents = True, exist_ok = True)
        if self._settings.include is not None:
            self._include = utils.load_trie(self._settings.include, self._settings.size)
        if self._settings.exclude is not None:
            self._exclude = utils.load_trie(self._settings.exclude, 1)

    def count(self) -> None:
        source_files = (path for path in utils.list_folder_documents(self._settings.source))
        source_files = utils.progress_overlay(source_files, 'Reading file #')
        lines = NGramCounter._read_lines_in_files(source_files)
        if not self._settings.keep_case:
            lines = NGramCounter._transform_case(lines)        
        xxx = [x for x in lines] # type: ignore
        pass

    @staticmethod
    def _read_lines_in_files(source_files: t.Iterator[pathlib.Path]) -> t.Iterator[t.List[str]]:
        for file in source_files:
            for line in utils.read_lines_in_file(file):
                arr = line.strip().split(' ')
                yield arr

    @staticmethod
    def _transform_case(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
        for line in lines:
            yield [tok.upper() for tok in line]
