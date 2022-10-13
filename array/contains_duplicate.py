from ast import List

# @see https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Simplest solution
        # return len(nums) != len(set(nums))

        # another solution
        # @see https://leetcode.com/problems/contains-duplicate/discuss/1077092/leetcode-217-contains-duplicate-easy-python-solution
        a = set()
        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                return True
        return False
