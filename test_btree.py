"""This script contains test cases to verify the correct behavior of a B-tree,
including insertion, searching, traversal, and integrity."""
import unittest
from trees.btree import BtreeNode


def load_not_insert_words():
    """Load words from 'data/not_insert_words.txt'."""
    with open("data/not_insert_words.txt", "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


class TestBtree(unittest.TestCase):
    """This class contains test cases to verify insertion, searching,
    and integrity of a B-tree."""

    def setUp(self):
        self.root = BtreeNode("x")

    def test_insert_and_search(self):
        """Tests insertion and exact searching functionality in the tree."""

        words = [
            "papaya", "mandarin", "lemon", "apple", "banana", "orange",
            "watermelon", "pineapple", "grape", "melon", "mango",
            "strawberry", "raspberry", "peach"
            ]

        for word in words:
            self.root._insert(word)

        for word in words:
            self.assertTrue(
                self.root._search(word), f"Search failed due to: {word}"
                )

        self.assertFalse(self.root._search("not_in_tree"))

    def test_in_order_traversal(self):
        """verify correct ordering of inserted words."""

        words = [
            "x", "tennis", "basketball", "badminton", "soccer",
            "cricket", "lacrosse", "rugby", "golf", "hockey",
            "baseball", "volleyball", "boxing", "table tennis"
            ]

        for word in words:
            self.root._insert(word)

        all_words = self.root._all_strings()
        expected_sorted = set(words)
        self.assertEqual(sorted(all_words), sorted(expected_sorted))

    def test_duplicates_not_inserted(self):
        """Tests that duplicate insertions do not create multiple entries."""
        self.root._insert("x")  # Duplicate of root
        self.root._insert("x")  # Again
        result = self.root._all_strings()
        self.assertEqual(result.count("x"), 1)

    def test_len_function(self):
        """Tests the length function to verify
        the correct count of stored words."""
        words = ["haircut", "make-up", "cardiology"]
        for word in words:
            self.root._insert(word)
        self.assertEqual(len(self.root), 4)

    def test_words_not_inserted(self):
        """Ensure words from 'not_insert_words.txt' are not found."""
        not_insert_words = load_not_insert_words()
        for word in not_insert_words:
            self.assertFalse(
                self.root._search(word), f"{word} should not be found"
                )


if __name__ == '__main__':
    unittest.main()
