from VLNGramCounter.utils import tokenize_lines, transform_case

def test_tokenize_lines():
    t0 = ['a', 'a b', 'a  b']
    t1 = (x for x in t0)
    res = list(tokenize_lines(t1))
    assert len(res) == 3
    assert res[0] == ['a']
    assert res[1] == ['a', 'b']
    assert res[2] == ['a', '', 'b']

def test_transform_case():
    t0 = [['a'], ['a','bb'], ['AaA']]
    t1 = (x for x in t0)
    res = list(transform_case(t1))
    assert len(res) == 3
    assert res[0] == ['A']
    assert res[1] == ['A', 'BB']
    assert res[2] == ['AAA']
