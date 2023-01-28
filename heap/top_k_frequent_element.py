# about heap: https://medium.com/basecs/learning-to-love-heaps-cef2b273a238
# solution: https://zhenyu0519.github.io/2020/07/11/lc347/

import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # https://qiita.com/ell/items/259388b511e24625c0d7
        dict = collections.Counter(nums)
        # about heapq: https://qiita.com/ell/items/fe52a9eb9499b7060ed6
        for val, count in dict.items():
            if len(res) < k:
                heapq.heappush(res, (count, val))
            else:
                heapq.heappush(res, (count, val))
                heapq.heappop(res)
        return [val for count, val in res]
