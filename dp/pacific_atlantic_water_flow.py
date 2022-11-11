# @see https://github.com/ChenglongChen/LeetCode-3/blob/master/Python/pacific-atlantic-water-flow.py

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # each height[r][c] can flow to same or less than to current cell's height.
        # return the indexes which can flow to both of Pacific and Atlantic Oceans.
        # ? なんで Pacific: 1, Atlantic: 2なんだ ？ heightと被らない？
        # -> visited (0と比べていく)
        # ORで計算する　登場するのは Pacific: 01, Atlantic: 10, visited: 00
        # pacific, atlanticを区別するために 01, 10の2桁で区別している
        PACIFIC, ATLANTIC = 1, 2

        def helper(
            matrix: List[List[int]],
            x: int,
            y: int,
            prevHeight: int,
            prevVal: int,
            visited: List[List[int]],
            res: List[List[int]],
        ):
            if (
                (not 0 <= x < len(matrix))  # xがまだ今のループのmatrix内
                or (not 0 <= y < len(matrix[0]))  # yもmatrix内
                or (matrix[x][y] < prevHeight)  # 移動する前の高さ これより小さければ、進むことができる
                # | １個だとどうなるんだっけ -> bit演算の OR になる
                # visited[x][y] -> 00 | 01 (pacific) -> 01 == 00
                # -> 🔵 わかった prevValは、もう訪れたかどうかを判定しているんだ　だからこの時はreturnする
                or (visited[x][y] | prevVal) == visited[x][y]
            ):
                return

            # visited[x][y] | prevVal を代入
            # visitedは　最初, matrix (height)のサイズの [0] の配列
            #
            visited[x][y] |= prevVal
            # pacific | atlantic -> 01 | 10 -> 11
            # つまり、visited[x][y]は 11 でどっちからも流れ込んだ形跡があるよ、ということ
            # そのx, yは PACIFIC, ATLANTICどちらからも来ているので、
            if visited[x][y] == (PACIFIC | ATLANTIC):
                res.append((x, y))

            for d in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                helper(
                    matrix,
                    x + d[0],
                    y + d[1],
                    matrix[x][y],  # ? matrixってなんだ？ -> prevHeight
                    visited[x][y],
                    visited,
                    res,
                )

        if not heights:
            return []

        res = []
        m, n = len(heights), len(heights[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            # float("-inf") はありえない数値として使用しているみたい
            # print(1 < float("-inf")) -> 必ずfalseになる
            # -1 と同義

            # ? xは固定で、mの場合は row つまり、どういうこと？
            # heights: matrix <- これはhelper内でもずっと変化することはない
            # ループは普通に左上と右上から行って、並列実行させる　[ -> <- ]
            helper(
                heights, i, 0, float("-inf"), PACIFIC, visited, res
            )  # 左から攻めるので prevVal: PACIFIC: 1
            helper(
                heights, i, n - 1, float("-inf"), ATLANTIC, visited, res
            )  # 右から攻めるので prevVal: ATLANTIC: 2
        for j in range(n):
            helper(heights, 0, j, float("-inf"), PACIFIC, visited, res)
            helper(heights, m - 1, j, float("-inf"), ATLANTIC, visited, res)

        return res
