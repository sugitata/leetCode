# @see https://github.com/awaemmanuel/LeetCode-Kamyu/blob/master/Python/spiral-matrix.py
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if matrix == []:
            return matrix

        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        # ? なぜ ++している？
        while top <= bottom or left <= right:
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            for i in range(top + 1, bottom):
                result.append(matrix[i][right])
            # 右から左に走査するのでreversed()
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    result.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    result.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return result
