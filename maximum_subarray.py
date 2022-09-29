# @see https://leetcode.com/problems/maximum-subarray/
# @see https://leetcode.com/problems/maximum-subarray/discuss/200180/python-with-explanation
class Solution:
    # it is DP problem
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        sumResult = [0 for i in range(len(nums))]
        sumResult[0] = nums[0]

        for i in range(1, len(nums)):
            if sumResult[i - 1] < 0:
                sumResult[i] = nums[i]
            else:
                sumResult[i] = sumResult[i - 1] + nums[i]
        return max(sumResult)
