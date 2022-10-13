from typing import List

# @see https://medium.com/codex/leetcode-152-maximum-product-subarray-python-solution-f30f7c4e76f3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod, min_prod, ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            tmp = max_prod
            max_prod = max(max_prod * nums[i], min_prod * nums[i], nums[i])
            min_prod = min(tmp * nums[i], min_prod * nums[i], nums[i])
            ans = max(ans, max_prod)
        return ans
