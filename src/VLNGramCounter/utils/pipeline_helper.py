import string
import typing as t
from ..dtypes import trie

def tokenize_lines(lines: t.Iterator[str]) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield line.strip().split(' ')

def transform_case(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield [tok.upper() for tok in line]

def clean_punct(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield [tok.strip(string.punctuation) for tok in line]

def remove_exclusions(lines: t.Iterator[t.List[str]], excludes: trie) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield [line[i] for i in range(0, len(line)) if not excludes.contains(line, i)]
