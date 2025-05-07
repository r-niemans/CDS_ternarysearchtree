""""This is a ternary search tree implemented
using object-oriented programming."""


class TtreeNode:
    """This object is a node in a ternary search tree (TST)."""

    def __init__(self, character=None):
        """Initialisation of the node"""
        self._character = character
        self._lt = None
        self._gt = None
        self._equals = None
        self.is_end = False

    def _insert(self, word, index=0):
        """Insertion of words via their characters in the TST."""
        if index == len(word):
            self.is_end = True
            return
        char = word[index]      # per character and not full string
        if self._character is None:
            self._character = char
        if char < self._character:
            if self._lt is None:
                self._lt = TtreeNode(char)
            self._lt._insert(word, index)
        elif char > self._character:
            if self._gt is None:
                self._gt = TtreeNode(char)
            self._gt._insert(word, index)
        else:
            if self._equals is None:
                self._equals = TtreeNode()
            self._equals._insert(word, index + 1)

    def _search(self, word, index=0, exact=False):  # exact parameter added
        """Search for words (when exact is True)
        or prefixes (when exact is False)."""
        if word == '' and not exact:
            return True
        if index == len(word):
            return self.is_end if exact else True
        char = word[index]
        if self._character is None:
            return False
        if char < self._character:
            return self._lt is not None and (
                self._lt._search(word, index, exact)
                )
        elif char > self._character:
            return self._gt is not None and (
                self._gt._search(word, index, exact)
                )
        else:
            return self._equals is not None and (
                self._equals._search(word, index + 1, exact)
                )

    def _collect_words(self, results, prefix=""):
        """Collect all words stored in the ternary search tree."""
        if self.is_end:
            results.append(prefix)
        if self._lt:
            self._lt._collect_words(results, prefix)
        if self._equals:
            self._equals._collect_words(results, prefix + self._character)
        if self._gt:
            self._gt._collect_words(results, prefix)

    def _all_strings(self):
        """Retrieve all words stored in the tree."""
        results = []
        self._collect_words(results, "")
        return results

    def __len__(self):
        """Calculate the number of nodes in the tree"""
        length = 1 if self.is_end else 0
        if self._lt:
            length += len(self._lt)
        if self._equals:
            length += len(self._equal)
        if self._gt:
            length += len(self._gt)
        return length

    def _to_string(self, prefix=''):
        """String representation of the tree"""
        repr_str = prefix + repr(self)
        if self._lt:
            repr_str += '\n' + self._lt._to_string(prefix + '  ')
        if self._equals:
            repr_str += '\n' + self._equal._to_string(prefix + '  ')
        if self._gt:
            repr_str += '\n' + self._gt._to_string(prefix + '  ')
        return repr_str

    def __repr__(self):
        """String representation of the node"""
        return f"Node({self._character}, boolean={self.is_end})"


class TernarySearchTree:
    """Ternary Search tree search for storing words"""

    def __init__(self):
        """Initialisation of an empty ternary search tree"""
        self._root = TtreeNode()
        self._size = 0

    def insert(self, word):
        """Insert a word into the ternary search tree"""
        if not self.search(word, exact=True):
            self._size += 1
        self._root._insert(word)

    def search(self, word, exact=False):
        """Search for a word or prefix in the tree"""
        if self._root is None:
            return False
        else:
            return self._root._search(word, exact=exact)

    def all_strings(self):
        """Retrieve all words stored in the tree."""
        return self._root._all_strings()

    def __len__(self):
        """Return the number of unique words in the tree."""
        return self._size

    def __repr__(self):
        """String representation of the tree"""
        if self._root is None:
            return 'empty tree'
        return self._root._to_string('')
