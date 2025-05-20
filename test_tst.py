import pytest
from trees.ternary_tree import TernarySearchTree


@pytest.mark.parametrize("word_list", [
    (["pizza", "cars", "can", "doll", "dormroom"]),
    (["avocado", "arsenal", "apextwin"]),
])
def test_basic_insert_and_search(word_list):
    tst = TernarySearchTree()
    for word in word_list:
        tst.insert(word)
    for word in word_list:
        assert tst.search(word, exact=True), f"{word} not found"
    assert not tst.search('', exact=True), 'Empty string should not be found'

# for the binary tree

def test_b_tree():
  tree = Node(1,
        Node(2,
           Node(3),
           Node(4,
              Node(6),
              None  # could be omitted but since it's an unbalanced node, being clear
           )
        ),
        Node(5)
      )
  assert [node.value for node in traverse_in_place_recursive(tree)] == [3, 2, 6, 4, 1, 5]