# @see https://python.plainenglish.io/rotate-image-day-80-python-bc215cc8e84b
# 1. matrix[]に対して、reverseして上下のrow位置を入れ替える
# 2. x, y座標をそれぞれのマスを入れ替える(ｙ＝ｘの直線に関する対称移動)
#   @see http://www.geisya.or.jp/~mwm48961/kou2/linear_trance1.html
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        # なんかうまくいかない
        # tmp = matrix
        # for x in range(len(matrix[0])):
        #     for y in range(len(matrix)):
        #         matrix[x][y] = tmp[y][x]
        for x in range(len(matrix)):
            # squareだから i = j
            for y in range(x):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
