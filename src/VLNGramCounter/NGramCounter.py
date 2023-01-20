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
            self._include = utils.load_map(self._settings.include, self._settings.length)
        if self._settings.exclude is not None:
            self._exclude = utils.load_map(self._settings.exclude, 1)

    def count(self) -> None:
        source_files = utils.list_folder_documents(self._settings.source)
        lines = utils.read_lines_in_files(source_files)
        lines = utils.progress_overlay(lines, 'Reading line #')
        token_lines = utils.tokenize_lines(lines)
        if not self._settings.keep_case:
            token_lines = utils.transform_case(token_lines)
        if not self._settings.keep_punct:
            token_lines = utils.clean_punct(token_lines)
        if self._settings.exclude is not None:
            token_lines = utils.remove_exclusions(token_lines, self._exclude)
        token_lines = utils.remove_empty_tokens(token_lines)
        ngrams = utils.collect_ngrams(token_lines, self._settings.length)
        if self._settings.include is not None:
            ngrams = utils.limit_inclusions(ngrams, self._include)
        ngram_chunks = utils.chunk_ngrams(ngrams, self._settings.max_ram)
        chunk_paths = list(utils.write_ngram_chunks(ngram_chunks, self._settings.cache_dir))
        chunk_path = utils.merge_sort_csv(chunk_paths, self._settings.cache_dir)
        ngrams = utils.read_csv_file(chunk_path)
        ngrams = utils.progress_overlay(ngrams, 'Reviewing N-Grams #')
        ngrams = utils.aggregate_ngrams(ngrams)
        ngrams = utils.apply_cutoff(ngrams, self._settings.cutoff)
        ngrams = utils.keep_top_ngrams(ngrams, self._settings.top)
        ngrams = (x for x in sorted(ngrams, key = lambda ng: ng[1], reverse = True))
        utils.write_ngrams(ngrams, self._settings.dest, self._settings.length)
        shutil.rmtree(self._settings.cache_dir)
