import shutil
from .dtypes import settings, trie
from .utils import load_trie

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
            self._include = load_trie(self._settings.include, self._settings.size)
        if self._settings.exclude is not None:
            self._exclude = load_trie(self._settings.exclude, 1)

    def count(self) -> None:
        pass

