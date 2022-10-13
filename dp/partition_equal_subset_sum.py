from collections import defaultdict


class Solution:
    # cache is for DP (memoize)
    def helper(self, i, array, target, cache):
        if target == 0:
            return True
        elif target < 0 or i == len(array):
            return False
        else:
            if i in cache and target in cache[i]:
                return cache[i][target]
            else:
                # call recursive (self) due to DP
                cache[i][target] = self.helper(i + 1, array, target, cache)
                if target - array[i] >= 0:
                    cache[i][target] = cache[i][target] or self.helper(
                        i + 1, array, target - array[i], cache
                    )
                return cache[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # if sum is odd, it can't be divided
        if total & 1:
            return False
        else:
            target = total / 2
        # initialize cache by using dictionary (defaultdict(dict))
        return self.helper(0, nums, target, defaultdict(dict))
