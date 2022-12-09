# @see https://leetcode.com/problems/word-search/solutions/27820/Python-DFS-solution/
# it is a question by using (DFS) 深さ優先探索 depth first search
# https://qiita.com/drken/items/4a7869c5e304883f539b
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True

        return False

    def getWords(
        self,
        board: List[List[str]],
        word: str,
        i: int,
        j: int,
        visited: dict,
        pos: int = 0,
    ) -> bool:
        # 今のポジションが探索している文字の長さと一致したなら操作終了
        if pos == len(word):
            return True

        # 走査を打ち切る
        #
        # i < 0 or i == len(board) : 範囲内のrowか確認
        # j < 0 or j == len(board[0]) : 範囲内のcolumnか確認
        # visited.get : DFSでseenになっているか確認
        # word[pos] != board[i][j] : 今ターゲットにしているwordの一文字がboardの今seeしているものと合っているか
        if (
            i < 0
            or i == len(board)
            or j < 0
            or j == len(board[0])
            or visited.get((i, j))
            or word[pos] != board[i][j]
        ):
            return False

        # ? visitedってどういう型？
        # dict: https://note.nkmk.me/en/python-dict-create/
        visited[(i, j)] = True
        # ? なぜ or でresを取得する？
        # -> 四方向で一つでもTrueになるものがあれば走査終了と見做せるから (pos == len(word))
        res = (
            # 次の文字の探索を四方向に対して行う
            self.getWords(board, word, i, j - 1, visited, pos + 1)
            or self.getWords(board, word, i + 1, j, visited, pos + 1)
            or self.getWords(board, word, i, j + 1, visited, pos + 1)
            or self.getWords(board, word, i, j + 1, visited, pos + 1)
        )

        return res
