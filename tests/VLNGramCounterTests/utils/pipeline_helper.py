from VLNGramCounter.dtypes import trie
from VLNGramCounter.utils import tokenize_lines, transform_case, clean_punct, remove_exclusions

def test_tokenize_lines():
    t0 = ['a', 'a b', 'a  b', '']
    t1 = (x for x in t0)
    res = list(tokenize_lines(t1))
    assert len(res) == 4
    assert res[0] == ['a']
    assert res[1] == ['a', 'b']
    assert res[2] == ['a', '', 'b']
    assert res[3] == ['']

def test_transform_case():
    t0 = [['a'], ['a','bb'], ['AaA'], [''], []]
    t1 = (x for x in t0)
    res = list(transform_case(t1))
    assert len(res) == 5
    assert res[0] == ['A']
    assert res[1] == ['A', 'BB']
    assert res[2] == ['AAA']
    assert res[3] == ['']
    assert res[4] == []

def test_clean_punct():
    t0 = [['a'], ['a?'], ['?a'], ['?a?'], ['a?a'], ['a?a?'], ['?a', 'b?'], ['?'], [''], []]
    t1 = (x for x in t0)
    res = list(clean_punct(t1))
    assert len(res) == 10
    assert res[0] == ['a']
    assert res[1] == ['a']
    assert res[2] == ['a']
    assert res[3] == ['a']
    assert res[4] == ['a?a']
    assert res[5] == ['a?a']
    assert res[6] == ['a', 'b']
    assert res[7] == ['']
    assert res[8] == ['']
    assert res[9] == []

def test_remove_exclusions():
    ex = trie(1)
    ex.increment(['a'], 0)
    t0 = [['a'], ['b'], ['a', 'b'], ['b', 'a'], ['aa'], ['b', 'a', 'b'], [''], []]
    t1 = (x for x in t0)
    res = list(remove_exclusions(t1, ex))
    assert len(res) == 8
    assert res[0] == []
    assert res[1] == ['b']
    assert res[2] == ['b']
    assert res[3] == ['b']
    assert res[4] == ['aa']
    assert res[5] == ['b', 'b']
    assert res[6] == ['']
    assert res[7] == []
