# @see https://leetcode.com/problems/set-matrix-zeroes/solutions/1414441/pythonpython3-set-matrix-zeros/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 1. 左端列、上端行は特別扱いして考える
        # 2. 左上端のマスはその十字放射状に0があるなら、0にしておく
        # 2. 左上端以外のマスは、左上端が0になっているなら、全部0にできる
        # 2. 最後は左上端に関して is_col, is_rowフラグによって0にするか考える
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        is_row = False

        for i in range(len(matrix[0])):
            # ? なんで１行目の0だけ確認している？
            # -> 一個でも行に0があったら、is_colをTrueにする
            # ? 何で？
            # -> 最後にその列を全部 0 にする
            if matrix[0][i] == 0:
                is_col = True

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_row = True

        # レコードは0から
        for i in range(len(matrix)):
            # ? なぜ列は1から？
            for j in range(1, len(matrix[0])):
                # そのマスが0なら、その左、上端っこのマスも0にしておく
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # col
                    matrix[0][j] = 0  # row

        # 左上端っこ以外のマスを全部0にしていく作業　（左上どちらかの端が0なら）
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                # さっき端っこを0にしたけど、実際、そのマスの端っこが0なら、そのマスも0にできる
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # 端っこに0ができるので、is_row, is_colのフラグによって端っこを全部 0 にできる
        if is_row:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        if is_col:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
