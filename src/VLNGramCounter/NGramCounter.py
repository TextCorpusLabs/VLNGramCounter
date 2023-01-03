import shutil
from . import utils
from .dtypes import settings

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
        lines = utils.read_lines_in_files(source_files)
        token_lines = utils.tokenize_lines(lines)
        if not self._settings.keep_case:
            token_lines = utils.transform_case(token_lines)
        if not self._settings.keep_punct:
            token_lines = utils.clean_punct(token_lines)
        if self._settings.exclude is not None:
            token_lines = utils.remove_exclusions(token_lines, self._exclude)
        token_lines = utils.remove_empty_tokens(token_lines)
        ngram_starts = utils.collect_ngram_starts(token_lines, self._settings.size)
        
        xxx = [x for x in ngram_starts] # type: ignore
        pass


