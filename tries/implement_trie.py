# @see https://www.geeksforgeeks.org/trie-insert-and-search/
# @see https://leetcode.com/problems/implement-trie-prefix-tree/solutions/127843/official-solution/
class TrieNode:
    def __init__(self):
        # ? Are they multiple arrays?
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self._initNode()

    def _initNode(self) -> TrieNode:
        return TrieNode()

    def _getCarIndex(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def insert(self, word: str) -> None:
        last_node = self.root
        for level in range(len(word)):
            i = self._getCarIndex(word[level])
            if not last_node.children[i]:
                last_node.children[i] = self._initNode()
            last_node = last_node.children[i]

        last_node.isEndOfWord = True

    def _searchPrefix(self, word: str) -> TrieNode:
        last_node = self.root
        for level in range(len(word)):
            i = self._getCarIndex(word[level])
            if not last_node.children[i]:
                return None
            last_node = last_node.children[i]
        return last_node

    def search(self, word: str) -> bool:
        node = self._searchPrefix(word)
        return node and node.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self._searchPrefix(prefix)
        return node is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
