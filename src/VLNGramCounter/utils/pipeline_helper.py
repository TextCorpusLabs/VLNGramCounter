import typing as t

def tokenize_lines(lines: t.Iterator[str]) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield line.strip().split(' ')

def transform_case(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        yield [tok.upper() for tok in line]
