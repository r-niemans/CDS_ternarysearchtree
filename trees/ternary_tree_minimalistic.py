"""
Sparse tree since you create nodes as you build the tree essentially only building what you need.
Higher in terms of saving memory but more costly time-wise due to the dict look-ups
"""
class TSTNode:
    def __init__(self, character=None):
        self.character = character
        self.children = {}  # this contains the nodes so {'lt': node, 'eq': node, 'gt': node}
        self.is_end = False


class TernarySearchTreeSparse:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, word):
        if not word:
            return
        if not self.root:
            self.root = TSTNode()

        current = self.root
        index = 0

        while index < len(word):
            char = word[index]

            if current.character is None:
                current.character = char

            if char < current.character:
                direction = 'lt'
            elif char > current.character:
                direction = 'gt'
            else:
                direction = 'eq'

            if direction not in current.children:
                current.children[direction] = TSTNode()

            current = current.children[direction]

            if direction == 'eq':
                index += 1

        if not current.is_end:
            current.is_end = True
            self.size += 1

    def search(self, word, exact=False):
        if not self.root or not word:
            return False

        current = self.root
        index = 0

        while current and index < len(word):
            if current.character is None:
                return False

            char = word[index]

            if char < current.character:
                direction = 'lt'
            elif char > current.character:
                direction = 'gt'
            else:
                direction = 'eq'

            current = current.children.get(direction)

            if direction == 'eq':
                index += 1

        if not current:
            return False
        return current.is_end if exact else True

    def all_strings(self):
        if not self.root:
            return []

        stack = [(self.root, "")]
        results = []

        while stack:
            current, prefix = stack.pop()

            if current.is_end:
                results.append(prefix)

            for direction, child in current.children.items():
                if direction == 'eq':
                    stack.append((child, prefix + current.character))
                else:
                    stack.append((child, prefix))

        return results

    def __len__(self):
        return self.size
