# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 26
#         self.isEndOfWord = False


# class WordDictionary:
#     def __init__(self):
#         self.root = self._initNode()

#     def _initNode(self):
#         return TrieNode()

#     def _getCharIndex(self, ch: str) -> int:
#         return ord(ch) - ord("a")

#     # How is this related to TRIE?
#     def addWord(self, word: str) -> None:
#         last_node = self.root
#         for level in range(len(word)):
#             i = self._getCharIndex(word[level])
#             if not last_node.children[i]:
#                 last_node.children[i] = self._initNode()
#             last_node = last_node.children[i]
#         last_node.isEndOfWord = True

#     # @see https://medium.com/coding-memo/leetcode-design-add-and-search-words-data-structure-a733e67c49da
#     def search(self, word: str) -> bool:
#         return self._match(self.root, word, 0)

#     def _match(self, node: TrieNode, word: str, index: int) -> bool:
#         if index == len(word):
#             return node.isEndOfWord == True
#         if word[index] == ".":
#             for child in node.children:
#                 if (
#                     child is not None
#                     and not child.isEndOfWord
#                     and self._match(child, word, index + 1)
#                 ):
#                     return True
#             return False

#         i = self._getCharIndex(word[index])
#         if not node.children[i]:
#             print("falseにします")
#             return False
#         return self._match(node, word, index + 1)


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)


class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["#"] = True

    # @see https://medium.com/coding-memo/leetcode-design-add-and-search-words-data-structure-a733e67c49da
    def search(self, word: str) -> bool:
        return self._match(self.trie, word, 0)

    def _match(self, node, word, i) -> bool:
        if i == len(word):
            return "#" in node

        if word[i] == ".":
            for child in node:
                # dfs
                if child != "#" and self._match(node[child], word, i + 1):
                    return True
            return False

        if word[i] not in node:
            return False
        return self._match(node[word[i]], word, i + 1)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
