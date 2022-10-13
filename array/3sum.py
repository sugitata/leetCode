# @see https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, result = len(nums), []
        for i in range(n):
            # e.g [2, 2, 4] at i == 1
            # ? why ... ?
            # ! -> Handling Duplicates in 3SUM
            if i > 0 and nums[i] == nums[i - 1]:
                # skip below process
                continue
            target = nums[i] * -1
            # start: next element
            # end: last element
            start, end = i + 1, n - 1
            # approaching between start and end gradually
            # [start -> <- end]
            while start < end:
                # e.g. [4, 2 , 3, 2]
                if nums[start] + nums[end] == target:
                    # e.g. [4, 2, 2]
                    # ? why??
                    result.append([nums[i], nums[start], nums[end]])
                    start = start + 1
                    # e.g. [4, 2, 2, 3]
                    # ? why??
                    # ! -> Handling Duplicates in 2SUM
                    while start < end and nums[start] == nums[start - 1]:
                        start = start + 1
                elif nums[start] + nums[end] < target:
                    start = start + 1
                else:
                    end = end - 1
        return result
