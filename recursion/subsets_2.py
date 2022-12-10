from typing import List

# @see https://github.com/ChenglongChen/LeetCode-3/blob/master/Python/subsets-ii.py
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # 最初に空の配列が最初に絶対入るので、それは入れておく
        res = [[]]
        previous_size = 0
        for i in range(len(nums)):
            size = len(res)
            for j in range(size):
                # i == 0 ならまだ nums[i-1] のことを考えなくていいから?
                # ? nums[i] != nums[i-1] だったら、そのsizeにおいて重複しているものを入れてしまうことになるから？
                # ? previous_size よりjが大きくないと、すでに重複しているものを入れていることにな流？
                if i == 0 or nums[i] != nums[i - 1] or j >= previous_size:
                    res.append(list(res[j]))
                    # ? 先頭に追加するってことかな？
                    # -> https://stackoverflow.com/questions/11367902/negative-list-index
                    # -> 逆だった最後の要素って意味らしい
                    # res[j] を append したので、さらにそこにユニークとなるターゲット値(nums[i])を追加してあげる
                    res[-1].append(nums[i])
            previous_size = size
        return res
