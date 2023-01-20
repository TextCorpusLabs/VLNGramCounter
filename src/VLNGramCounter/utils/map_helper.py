import pathlib
import typing as t

def load_map(path: pathlib.Path, size: int) -> t.Set[str]:
    result: t.Set[str] = set[str]()
    with open(path, 'r', encoding = 'utf-8') as fp:
        for line in fp:
            arr = line.strip().split(' ')            
            if len(arr) != size:
                print(f'Wrong number of elements. Expected {size} found {len(arr)} in {line}')
                continue
            val = ' '.join(arr)
            result.add(val)
    return result
