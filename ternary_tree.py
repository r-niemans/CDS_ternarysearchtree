class TtreeNode:

    def __init__(self, character=None):
        self._character = character
        self._lt = None
        self._gt = None
        self._equal = None
        self.is_end = False

    def _insert(self, word, index=0):
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
            if self._equal is None:
                self._equal = TtreeNode()
            self._equal._insert(word, index + 1)

    def _search(self, word, index=0, exact=False):  # exact parameter added
        if word == '' and not exact:
            return True
        if index == len(word):
            return self.is_end if exact else True
        char = word[index]
        if self._character is None:
            return False
        if char < self._character:
            return self._lt is not None and self._lt._search(word, index, exact)
        elif char > self._character:
            return self._gt is not None and self._gt._search(word, index, exact)
        else:
            return self._equal is not None and self._equal._search(word, index + 1, exact)


    def _collect_words(self, results, prefix):
        if self.is_end:
            results.append(prefix)
        if self._lt:
            self._lt._collect_words(results, prefix)
        if self._equal:
            self._equal._collect_words(results, prefix + self._character)
        if self._gt:
            self._gt._collect_words(results, prefix)

    def _all_strings(self):
        results = []
        self._collect_words(results, "")
        return results


    def __len__(self):
        length = 1
        if self._lt is not None:
            length += len(self._lt)
        if self._equal is not None:
            length += len(self._equal)
        if self._gt is not None:
            length += len(self._gt)
        return length

    def _to_string(self, prefix=''):
        repr_str = prefix + repr(self)
        if self._lt:
            repr_str += '\n' + self._lt._to_string(prefix + '  ')
        if self._equal:
            repr_str += '\n' + self._equal._to_string(prefix + '  ')
        if self._gt:
            repr_str += '\n' + self._gt._to_string(prefix + '  ')
        return repr_str

    def __repr__(self):
        return f"Node({self._character}, boolean={self.is_end})"


class TernarySearchTree:

    def __init__(self):
        self._root = TtreeNode()
        self._size = 0

    def insert(self, word):
        if not self.search(word, exact=True):
            self._size += 1
        self._root._insert(word)


    def search(self, word, exact=False):
        if self._root is None:
            return False
        else:
            return self._root._search(word, exact=exact)

        
    def all_strings(self):
        return self._root._all_strings()
        
    def __len__(self):
        return self._size

    
    def __repr__(self):
        if self._root is None:
            return 'empty tree'
        else:
            return self._root._to_string()