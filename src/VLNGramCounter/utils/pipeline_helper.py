import string
import typing as t
from sys import maxsize as MAX_SIZE

def apply_cutoff(ngrams: t.Iterator[t.Tuple[str, int]], cutoff: int) -> t.Iterator[t.Tuple[str, int]]:
    for ngram in ngrams:
        if ngram[1] >= cutoff:
            yield ngram

def aggregate_ngrams(ngrams: t.Iterator[t.List[str]]) -> t.Iterator[t.Tuple[str, int]]:
    prev_gram: str | None = None
    prev_cnt: int = 0
    for ngram in ngrams:
        if prev_gram is None:
            prev_gram = ngram[0]
            prev_cnt = int(ngram[1])
        elif prev_gram == ngram[0]:
            prev_cnt += int(ngram[1])
        else:
            yield (prev_gram, prev_cnt)
            prev_gram = ngram[0]
            prev_cnt = int(ngram[1])
    if prev_gram is not None:
        yield (prev_gram, prev_cnt)

def chunk_ngrams(ngrams: t.Iterator[str], chunk_size: int) -> t.Iterator[t.Dict[str, int]]:
    chunk: t.Dict[str, int] = {}
    chunk_i: int = 0
    for ngram in ngrams:
        if ngram in chunk:
            chunk[ngram] += 1
        else:
            chunk[ngram] = 1
            chunk_i += 1
        if chunk_i >= chunk_size:
            yield chunk
            chunk = {}
            chunk_i = 0
    if chunk_i >= 0:
        yield chunk

def clean_punct(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok.strip(string.punctuation) for tok in line]
        yield res

def collect_ngrams(lines: t.Iterator[t.List[str]], size: int) -> t.Iterator[str]:
    for line in lines:
        if len(line) >= size:
            for i in range(0, len(line) - size + 1):
                res = ' '.join(line[i:(i+size)])
                yield res

def keep_top_ngrams(ngrams: t.Iterator[t.Tuple[str, int]], top: int) -> t.Iterator[t.Tuple[str, int]]:
    def _add(results: t.Dict[int, t.List[t.Tuple[str, int]]], ngram: t.Tuple[str, int]):
        if ngram[1] not in results:
            results[ngram[1]] = []
        results[ngram[1]].append(ngram)
    results: t.Dict[int, t.List[t.Tuple[str, int]]] = {}
    cnt = 0
    mn = MAX_SIZE
    for ngram in ngrams:
        if cnt < top:
            _add(results, ngram)
            cnt = cnt + 1
            if ngram[1] < mn:
                mn = ngram[1]
        elif ngram[1] == mn:
            _add(results, ngram)
            cnt = cnt + 1
        elif ngram[1] > mn:
            _add(results, ngram)
            cnt = cnt + 1
            t1 = len(results[mn])
            if cnt - t1 >= top:
                del results[mn]
                cnt = cnt - t1
                mn = min(results.keys())
    for best_ngrams in results.values():
        for ngram in best_ngrams:
            yield ngram

def limit_inclusions(ngrams: t.Iterator[str], includes: t.Set[str]) -> t.Iterator[str]:
    for ngram in ngrams:
        if ngram in includes:
            yield ngram

def remove_empty_tokens(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok for tok in line if len(tok) > 0]
        if len(res) > 0:
            yield res

def remove_exclusions(lines: t.Iterator[t.List[str]], excludes: t.Set[str]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [item for item in line if item not in excludes]
        yield res

def reverse_ngrams(lists: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for list in lists:
        a = list[0]
        list[0] = list[1]
        list[1] = a
        yield list

def tokenize_lines(lines: t.Iterator[str]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = line.strip().split(' ')
        yield res

def transform_case(lines: t.Iterator[t.List[str]]) -> t.Iterator[t.List[str]]:
    for line in lines:
        res = [tok.upper() for tok in line]
        yield res