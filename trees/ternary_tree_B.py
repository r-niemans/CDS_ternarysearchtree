""""This is a ternary search tree implemented
using object-oriented programming using iterative principles."""


class TtreeNode:
    """This object is a node in a ternary search tree (TST)."""

    def __init__(self, character=None):
        """Initialisation of the node"""
        self.character = character
        self._lt = None
        self._gt = None
        self._equals = None
        self.is_end = False


class TernarySearchTreeB:
    """Ternary Search tree search for storing words"""
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, word):
        """Insertion of words via their characters in the TST."""
        if not self.root:
            self.root = TtreeNode()

        current = self.root
        index = 0

        while index < len(word):
            char = word[index]
            if current.character is None:
                current.character = char

            if char < current.character:
                if not current._lt:
                    current._lt = TtreeNode()
                current = current._lt
            elif char > current.character:
                if not current._gt:
                    current._gt = TtreeNode()
                current = current._gt
            else:
                if not current._equals:
                    current._equals = TtreeNode()
                current = current._equals
                index += 1

        if not current.is_end:
            current.is_end = True
            self.size += 1

    def search(self, word, exact=False):
        """Search for words (when exact is True)
        or prefixes (when exact is False)."""
        current = self.root
        index = 0

        while current and index < len(word):
            if current.character is None:
                return False

            char = word[index]
            if char < current.character:
                current = current._lt
            elif char > current.character:
                current = current._gt
            else:
                current = current._equals
                index += 1

        if not current:
            return False
        return current.is_end if exact else True

    def all_strings(self):
        """Retrieve all words stored in the tree."""
        if not self.root:
            return []

        stack = [(self.root, "")]
        results = []

        while stack:
            current, prefix = stack.pop()
            if current.is_end:
                results.append(prefix)
            if current._gt:
                stack.append((current._gt, prefix))
            if current._equals:
                stack.append((current._equals, prefix + current.character))
            if current._lt:
                stack.append((current._lt, prefix))

        return results

    def __len__(self):
        """Return the number of unique words in the tree."""
        return self.size

    def __repr__(self):
        """String representation of the tree"""
        if not self.root:
            return 'empty tree'
        stack = [(self.root, "")]
        repr_str = ""

        while stack:
            current, prefix = stack.pop()
            repr_str += f"{prefix}- {current.character} ({current.is_end})\n"
            if current._gt:
                stack.append((current._gt, prefix + "  "))
            if current._equals:
                stack.append((current._equals, prefix + "  "))
            if current._lt:
                stack.append((current._lt, prefix + "  "))

        return repr_str.strip()
