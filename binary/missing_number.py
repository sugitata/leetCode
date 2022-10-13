class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(0, len(nums) - 1):
            if nums[i] + 1 != nums[i + 1]:
                return nums[i] + 1
        return len(nums)


# other solution by using binary
# https://dxmahata.gitbooks.io/leetcode-python-solutions/content/missing-number.html
