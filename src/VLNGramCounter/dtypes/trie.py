import typing as t

class trie:

    class _node:
        __slots__ = ['value', 'children']
        def __init__(self):
            self.value: int = 0
            self.children: t.Dict[str, trie._node] = {}
    
    class item:
        __slots__ = ['item', 'freq']
        def __init__(self, item: t.List[str], freq: int):
            self.item: t.List[str] = item
            self.freq: int = freq

    def __init__(self, length: int):
        self._root: trie._node = trie._node()
        self._length = length
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def length(self):
        return self._length

    def increment(self, array: t.List[str], start: int) -> None:
        root: trie._node = self._root
        for i in range(0, self._length):
            key: str = array[start + i]
            if key not in root.children:
                root.children[key] = trie._node()
                self._size += len(key)
            root = root.children[key]
        root.value += 1

    def contains(self, array: t.List[str], start: int) -> bool:
        root: trie._node = self._root
        for i in range(0, self._length):
            key: str = array[start + i]
            if key not in root.children:
                return False
            root = root.children[key]
        return True

    def enumerate(self) -> t.Iterator[item]:
        def _helper(root: trie._node, pos: int, arr: t.List[str]) -> t.Iterator[trie.item]:
            if len(root.children) == 0:
                yield trie.item([i for i in arr], root.value)
            for key in sorted(root.children.keys()):
                arr[pos] = key
                for res in _helper(root.children[key], pos + 1, arr):
                    yield res
        arr: t.List[str] = ['' for _ in range(0, self._length)]
        for res in _helper(self._root, 0, arr):
            yield res
