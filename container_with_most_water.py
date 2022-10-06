class Solution:
    def maxArea(self, height: List[int]) -> int:
        #
        # O(n^2)
        #
        # area = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         area = max(area, min(height[i], height[j]) * (j - i))
        # return area

        #
        # O(n)
        #
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            area = max(area, ((right - left) * min(height[left], height[right])))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
