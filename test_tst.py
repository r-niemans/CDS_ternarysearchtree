import pytest
from ternary_tree import TernarySearchTree


@pytest.mark.parametrize("word_list", [
    (["cat", "cap", "can", "dog", "dorm"]),
    (["apple", "ape", "apex"]),
])
def test_basic_insert_and_search(word_list):
    tst = TernarySearchTree()
    for word in word_list:
        tst.insert(word)
    for word in word_list:
        assert tst.search(word, exact=True), f"{word} not found"
    assert not tst.search('', exact=True), 'Empty string should not be found'