import pathlib

class settings:

    def __init__(self, source: pathlib.Path, dest: pathlib.Path, size: int, control: int, include: pathlib.Path, exclude: pathlib.Path, cutoff:int, top: int, keep_case: bool, keep_punct: bool):
        """
        Settings for the ngram counter

        Parameters
        ----------
        source : pathlib.Path
            The folder containing the TXT files
        dest : pathlib.Path
            The CSV file used to store the ngram results
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
        self._source = source
        self._dest = dest
        self._size = size
        self._control = control
        self._include = include
        self._exclude = exclude
        self._cutoff = cutoff
        self._top = top
        self._keep_case = keep_case
        self._keep_punct = keep_punct

    @property
    def source(self) -> pathlib.Path:
        return self._source
    @property
    def dest(self) -> pathlib.Path:
        return self._dest
    @property
    def cache_dir(self) -> pathlib.Path:
        return self._dest.parent.joinpath(f'tmp_{self._dest.name}')        
    @property
    def size(self) -> int:
        return self._size
    @property
    def control(self) -> int:
        return self._control
    @property
    def include(self) -> pathlib.Path:
        return self._include
    @property
    def exclude(self) -> pathlib.Path:
        return self._exclude
    @property
    def cutoff(self) -> int:
        return self._cutoff
    @property
    def top(self) -> int:
        return self._top
    @property
    def keep_case(self) -> bool:
        return self._keep_case
    @property
    def keep_punct(self) -> bool:
        return self._keep_punct

    def validate(self) -> None:
        """
        Ensures the settings have face validity
        """
        def _folder(path: pathlib.Path) -> None:
            if not path.exists():
                raise ValueError(f'{str(path)} is does not exist')
            if not path.is_dir():
                raise ValueError(f'{str(path)} is not a folder')
        def _file(path: pathlib.Path) -> None:
            if path is not None:
                if not path.exists():
                    raise ValueError(f'{str(path)} is does not exist')
                if not path.is_file():
                    raise ValueError(f'{str(path)} is not a file')
        def _nonzero_int(val: int):
            if val <= 0:
                raise ValueError(f'{val} must be > 0')
        _folder(self._source)
        _folder(self._dest.parent)
        _nonzero_int(self._size)
        _nonzero_int(self._control)
        _file(self._include)
        _file(self._exclude)
        _nonzero_int(self._cutoff)
        _nonzero_int(self._top)
