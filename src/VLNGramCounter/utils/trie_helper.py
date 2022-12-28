import pathlib
from ..dtypes import trie

def load_trie(path: pathlib.Path, size: int) -> trie:
    result = trie(size)
    with open(path, 'r', encoding = 'utf-8') as fp:
        for line in fp:
            arr = line.strip().split(' ')
            if len(arr) != size:
                print(f'Wrong number of elements. Expected {size} found {len(arr)} in {line}')
                continue
            result.increment(arr, 0)
    return result
