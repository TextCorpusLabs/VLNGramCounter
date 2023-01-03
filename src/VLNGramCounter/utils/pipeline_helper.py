import string
import typing as t
from ..dtypes import trie

def clean_punct(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok.strip(string.punctuation) for tok in line]
        yield res

def collect_ngram_starts(lines: t.Iterator[t.List[str]], size: int) -> t.Iterator[t.Tuple[t.List[str], int]]:
    for line in lines:
        if len(line) >= size:
            for i in range(0, len(line) - size + 1):
                res = (line, i)
                yield res

def remove_empty_tokens(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok for tok in line if len(tok) > 0]
        if len(res) > 0:
            yield res

def remove_exclusions(lines: t.Iterator[t.List[str]], excludes: trie) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [line[i] for i in range(0, len(line)) if not excludes.contains(line, i)]
        yield res

def tokenize_lines(lines: t.Iterator[str]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = line.strip().split(' ')
        yield res

def transform_case(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok.upper() for tok in line]
        yield res