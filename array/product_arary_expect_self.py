from typing import List

# @see https://leetcode.com/problems/product-of-array-except-self/
# @see https://atharayil.medium.com/product-of-array-except-self-day-33-python-82030c2cc470
# We must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            output[i] = output[i - 1] * nums[i - 1]

        R = 1

        for i in range(len(output) - 1, -1, -1):
            output[i] = output[i] * R
            R = R * nums[i]

        return output
