class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1

        # e.g. [1, 2, 3, 4]
        if nums[start] < nums[end]:
            return nums[start]

        # during loop, approach between start and end
        # start -> mid <- end
        while start <= end:
            mid = int((start + end) / 2)
            # think from middle (binary tree search?)
            # e.g. [3, 1, 2]
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            # think to end
            # e.g. [3, 1, 2]
            if mid < (len(nums) - 1) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # start -> mid <- end
            if nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return nums[0]
