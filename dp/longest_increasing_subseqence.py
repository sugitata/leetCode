# @see https://www.geeksforgeeks.org/python-program-for-longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        # memoize the max the number of subsequence from 1 to n
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        # init
        maximum = 0
        for i in range(n):
            maximum = max(maximum, dp[i])
        return maximum
