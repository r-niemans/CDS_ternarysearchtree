import pytest
from trees.ternary_tree import TernarySearchTree
from trees.ternary_tree_B import TernarySearchTreeB
from trees.ternary_tree_recursive import TernarySearchTreeRecursive
from trees.ternary_tree_minimalistic import TernarySearchTreeSparse


@pytest.mark.parametrize("tree_class", [
    TernarySearchTree,
    TernarySearchTreeB,
    TernarySearchTreeRecursive,
    TernarySearchTreeSparse
])
@pytest.mark.parametrize("word_list", [
    (["pizza", "cars", "can", "doll", "dormroom"]),
    (["avocado", "arsenal", "apextwin"]),
])
def test_basic_insert_and_search(tree_class, word_list):
    """Check if inserted words can be found in the tree"""
    tst = tree_class()
    for word in word_list:
        tst.insert(word)
    for word in word_list:
        assert tst.search(word, exact=True), f"{word} not found"
    assert not tst.search('', exact=True), 'Empty string should not be found'


def load_not_insert_words():
    """Load words from 'data/not_insert_words.txt'."""
    with open("data/not_insert_words.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

@pytest.mark.parametrize("tree_class", [
    TernarySearchTree,
    TernarySearchTreeB,
    TernarySearchTreeRecursive,
    TernarySearchTreeSparse
])
def test_words_not_inserted(tree_class):
    """Ensure words from 'not_insert_words.txt' are not found."""
    tst = tree_class()
    not_insert_words = load_not_insert_words()

    for word in not_insert_words:
        assert not tst.search(word, exact=True), f"{word} should not be found"
