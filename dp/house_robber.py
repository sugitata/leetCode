# class Solution:
#     def rob(self, nums: List[int]) -> int:
# dp = [0] * (len(nums) + 1)
# dp = [0] * (len(nums))
# if len(nums) == 0:
#     return dp[0]
# ! これだとodd/eventでしか足し合わせてないから意味がない
# dp[1] = nums[0]
# if len(nums) == 1:
#     return dp[1]
# dp[2] = max(nums[0], nums[1])
# if len(nums) == 2:
#     return dp[2]

# for w in range(3, len(nums) + 1):
#     dp[w] = nums[w - 1] + dp[w - 2]
#     print(dp)
# return max(dp[len(nums) - 1], dp[len(nums)])

# for w in range(2, len(nums)):
#     dp[w] = max((nums[w] + dp[w - 2]), dp[w - 1])
# return dp[-1]

# @see https://atharayil.medium.com/house-robber-day-18-python-5e4d4f17f00e
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        dp = [0 for row in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max((nums[i] + dp[i - 2]), dp[i - 1])
        return dp[-1]
