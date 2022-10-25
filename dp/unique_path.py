# @see https://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1:
        #     return 1
        # return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

        # n: weight
        # m: value
        dp = [1] * n
        # ? なぜこうしている
        for w in range(1, m - 1):
            for v in range(1, n):
                dp[v] += dp[v - 1]
        return dp[-1]
