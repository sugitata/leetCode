# @see https://www.tutorialspoint.com/unique-paths-in-python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

        # m: weight (column)
        # n: value (row)
        column = m
        row = n
        dp = [[-1 for w in range(m)] for v in range(n)]
        # init
        # ? なぜこうしている
        # e.g. (m: 5, n: 4)
        # | -1 -1 -1 -1 -1|
        # | -1 -1 -1 -1 -1|
        # | -1 -1 -1 -1  1|
        # | -1 -1 -1 -1 -1|
        dp[row - 2][column - 1] = 1
        for w in range(column):
            # 最下段も1にする
            dp[row - 1][w] = 1
        for v in range(row):
            # 最右行も1にする
            dp[v][column - 1] = 1
        # ? rangeを３つとる場合は何？
        # ->
        for v in range(row - 2, -1, -1):
            for w in range(column - 2, -1, -1):
                # ? 逆算している？（右下のゴールからメモして行っている）
                dp[v][w] = dp[v + 1][w] + dp[v][w + 1]
        return dp[0][0]
