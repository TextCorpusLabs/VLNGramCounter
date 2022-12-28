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
        pass


    def count(self) -> None:
        pass

