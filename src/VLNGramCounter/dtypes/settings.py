import pathlib


class settings:

    def __init__(self, size: int, control: int, include: pathlib.Path, exclude: pathlib.Path, cutoff:int, top: int, keep_case: bool, keep_punct: bool):
        """
        Settings for the ngram counter

        Parameters
        ----------
        size :  int
            The length of the n-gram
        control: int
            The rough amount of ram (in Mb) used by the control structure
        include: pathlib.Path
            Count only values in this CSV list
        exclude: pathlib.Path
            Ignore values in this CSV list
        cutoff : int
            The minimum value count to keep
        top : int
            The number of n-grams to save
        keep_case: bool
            Keeps the casing as-is before converting to tokens
        keep_punct: bool
            Keeps all punctuation of the before converting to tokens
        """
        self._size = size
        self._control = control
        self._include = include
        self._exclude = exclude
        self._cutoff = cutoff
        self._top = top
        self._keep_case = keep_case
        self._keep_punct = keep_punct

    @property
    def size(self):
        return self._size
    @property
    def control(self):
        return self._control
    @property
    def include(self):
        return self._include
    @property
    def exclude(self):
        return self._exclude
    @property
    def cutoff(self):
        return self._cutoff
    @property
    def top(self):
        return self._top
    @property
    def keep_case(self):
        return self._keep_case
    @property
    def keep_punct(self):
        return self._keep_punct
