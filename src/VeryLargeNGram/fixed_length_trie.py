import typing as t

class fixed_length_trie:
    class Node:
        def __init__(self):
            pass

    def __init__(self, length: int):
        self._root: t.Dict[str, int] = {}
        self._length = length
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def length(self):
        return self._length

    def increment(self, array: t.List[str], start: int) -> None:
        pass 

    def contains(self, array: t.List[str], start: int) -> bool:
        return True

    def enumerate(self) -> t.Iterator[t.List[str]]:
        pass