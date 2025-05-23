""""This is a binary tree implemented
using object-oriented programming."""


class BtreeNode:
    """This object is a node in a binary tree."""

    def __init__(self, string):
        """Initialisation of the node"""
        self._string = string
        self._lt, self._gt = None, None

    def _insert(self, string):
        """Insertion of words via their characters in the binary tree."""
        if string == self._string:
            return
        if string < self._string:
            if self._lt is None:
                self._lt = BtreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = BtreeNode(string)
            else:
                self._gt._insert(string)

    def _search(self, string, exact=False):
        """Search for words (when exact is True)
        or prefixes (when exact is False)."""
        if self._string.startswith(string) and not exact:
            return True
        if self._string == string:
            return True

        if string < self._string and self._lt is not None:
            return self._lt._search(string, exact)
        elif string > self._string and self._gt is not None:
            return self._gt._search(string, exact)

        return False

    def _all_strings(self):
        """Retrieve all words stored in the tree."""
        strings = [self._string]
        if self._lt is not None:
            strings.extend(self._lt._all_strings())
        if self._gt is not None:
            strings.extend(self._gt._all_strings())
        return strings

    def __len__(self):
        """Calculate the number of nodes in the tree"""
        length = 1
        if self._lt is not None:
            length += len(self._lt)
        if self._gt is not None:
            length += len(self._gt)
        return length

    def _to_string(self, indent=''):
        """String representation of the tree"""
        repr_str = indent + repr(self)
        if self._lt is not None:
            repr_str += '\n' + self._lt._to_string(indent + '  ')
        if self._gt is not None:
            repr_str += '\n' + self._gt._to_string(indent + '  ')
        return repr_str

    def __repr__(self):
        """String representation of the node"""
        return self._string


class Btree:
    """Binary tree for storing words"""

    def __init__(self):
        """Initialisation of an empty binary tree"""
        self._root = None

    def insert(self, string):
        """Insert a word into the binary tree"""
        if self._root is None:
            self._root = BtreeNode(string)
        else:
            self._root._insert(string)

    def search(self, string, exact=False):
        """Search for a word or prefix in the tree"""
        if self._root is None:
            return False
        else:
            return self._root._search(string, exact)

    def all_strings(self):
        """Retrieve all words stored in the tree."""
        if self._root is None:
            return []
        else:
            return self._root._all_strings()

    def __len__(self):
        """Return the number of unique words in the tree."""
        if self._root is None:
            return 0
        else:
            return len(self._root)

    def __repr__(self):
        """String representation of the tree"""
        if self._root is None:
            return 'empty tree'
        else:
            return self._root._to_string('')
