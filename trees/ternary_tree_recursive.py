""""This is a reviewed version of a previously designed ternary search tree
implemented and differs in sense that it does not contain empty nodes and
slices strings recursively, therefore being more memory efficient
but making a function call heavier."""


class TSTNode:
    """This object is a node in a ternary search tree (TST)."""

    def __init__(self, char):
        """Initialisation of the node"""
        self.char = char
        self.last_char_in_string = False
        self.less_than = None
        self.equals = None
        self.larger_than = None

    def _insert(self, string):
        """Insertion of words via their characters in the TST."""
        char = string[0]

        if char < self.char:
            if self.less_than is None:
                self.less_than = TSTNode(char)
            self.less_than._insert(string)
        elif char > self.char:
            if self.larger_than is None:
                self.larger_than = TSTNode(char)
            self.larger_than._insert(string)
        elif len(string) > 1:
            if self.equals is None:
                self.equals = TSTNode(string[1])
            self.equals._insert(string[1:])
        else:
            self.last_char_in_string = True

    def _search(self, string):
        """Search for words"""
        if not string:
            return False
        char = string[0]

        if char < self.char:
            return self.less_than._search(string) if self.less_than else False
        elif char > self.char:
            return self.larger_than._search(string) if self.larger_than else False
        elif len(string) > 1:
            return self.equals._search(string[1:]) if self.equals else False
        else:
            return self.last_char_in_string

    def _all_strings(self, prefix=""):
        """Retrieve all strings stored in the node."""
        strings = []
        if self.last_char_in_string:
            strings.append(prefix + self.char)
        if self.less_than:
            strings.extend(self.less_than._all_strings(prefix))
        if self.equals:
            strings.extend(self.equals._all_strings(prefix + self.char))
        if self.larger_than:
            strings.extend(self.larger_than._all_strings(prefix))
        return strings

    def __len__(self):
        """Calculate the number of nodes in the tree"""
        length = 1 if self.last_char_in_string else 0
        if self.less_than:
            length += len(self.less_than)
        if self.equals:
            length += len(self.equals)
        if self.larger_than:
            length += len(self.larger_than)
        return length

    def _to_string(self, indent=''):
        """String representation of the node"""
        repr_str = indent + repr(self.char) + \
            ("*" if self.last_char_in_string else "")
        if self.equals:
            repr_str += '\n' + self.equals._to_string(indent + '  ')
        if self.less_than:
            repr_str += '\n' + self.less_than._to_string(indent + '  ')
        if self.larger_than:
            repr_str += '\n' + self.larger_than._to_string(indent + '  ')
        return repr_str


class TernarySearchTreeRecursive:
    """Ternary Search tree search for storing words"""

    def __init__(self):
        self.root = None

    def insert(self, string):
        """Initialisation of an empty ternary search tree"""
        if not self.root:
            self.root = TSTNode(string[0])
        self.root._insert(string)

    def search(self, string, exact=False):
        """Search for a word in the tree"""
        if exact:
            return self.root._search(string) if self.root else False
        return self.prefix_search(string) if self.root else []

    def prefix_search(self, prefix):
        """Search for a prefix in the tree"""
        results = []
        if not prefix:  # Check if prefix is empty
            node = self.root
        else:
            node = self._search_prefix_node(self.root, prefix, 0)
        if node:
            self._collect_strings(node, prefix, results)
        return results

    def _search_prefix_node(self, node, prefix, index):
        """Search for a prefix in the node"""
        if not node:
            return None

        char = prefix[index]
        if char < node.char:
            return self._search_prefix_node(node.less_than, prefix, index)
        elif char > node.char:
            return self._search_prefix_node(node.larger_than, prefix, index)
        elif index < len(prefix) - 1:
            return self._search_prefix_node(node.equals, prefix, index + 1)
        else:
            return node

    def _collect_strings(self, node, prefix, results):
        """Collect all words stored in the ternary search tree."""
        if node.last_char_in_string:
            results.append(prefix + node.char)

        if node.less_than:
            self._collect_strings(node.less_than, prefix, results)
        if node.equals:
            self._collect_strings(node.equals, prefix + node.char, results)
        if node.larger_than:
            self._collect_strings(node.larger_than, prefix, results)

    def count_strings(self):
        """Count the strings in the ternary search tree."""
        return len(self)

    def all_strings(self):
        """Retrieve all words stored in the tree."""
        return self.prefix_search("")

    def __len__(self):
        """Return the number of unique words in the tree."""
        return len(self.root) if self.root else 0

    def __repr__(self):
        """String representation of the tree"""
        return self.root._to_string() if self.root else 'empty'
