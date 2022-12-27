from VeryLargeNGram import fixed_length_trie

def test_length():
    x = fixed_length_trie(1)
    assert x.length == 1

