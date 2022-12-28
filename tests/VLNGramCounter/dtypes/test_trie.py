from VLNGramCounter.dtypes import trie

def test_length():
    obj = trie(1)
    assert obj.length == 1

def test_size():
    obj = trie(1)
    assert obj.size == 0

def test_increment_basic_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert obj.size == 1

def test_increment_more_same_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    obj.increment(arr, 0)
    assert obj.size == 1

def test_increment_more_different_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    assert obj.size == 2

def test_increment_basic_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert obj.size == 1

def test_increment_shared_len2():
    obj = trie(2)
    arr = ['a', 'a', 'b']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    assert obj.size == 2

def test_increment_more_same_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    obj.increment(arr, 0)
    assert obj.size == 1

def test_increment_more_different_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    assert obj.size == 2

def test_enumerate_basic_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    res = [i for i in obj.enumerate()]
    assert len(res) == 1
    assert res[0].item ==  ['a']
    assert res[0].freq == 1

def test_enumerate_basic_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    res = [i for i in obj.enumerate()]
    assert len(res) == 2
    assert res[0].item ==  ['a', 'b']
    assert res[0].freq == 1
    assert res[1].item ==  ['b', 'c']
    assert res[1].freq == 1

def test_enumerate_shared_len2():
    obj = trie(2)
    arr = ['a', 'a', 'b']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    res = [i for i in obj.enumerate()]
    assert len(res) == 2
    assert res[0].item ==  ['a', 'a']
    assert res[0].freq == 1
    assert res[1].item ==  ['a', 'b']
    assert res[1].freq == 1

def test_contains_basic_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert obj.contains(['a'], 0)

def test_contains_not_basic_len1():
    obj = trie(1)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert not obj.contains(['b'], 0)

def test_contains_basic_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert obj.contains(['a', 'b'], 0)

def test_contains_not_basic_len2():
    obj = trie(2)
    arr = ['a', 'b', 'c']
    obj.increment(arr, 0)
    assert not obj.contains(['b', 'c'], 0)

def test_contains_shared_len2():
    obj = trie(2)
    arr = ['a', 'a', 'b']
    obj.increment(arr, 0)
    obj.increment(arr, 1)
    assert obj.contains(['a', 'a'], 0)
    assert obj.contains(['a', 'b'], 0)
