# @see https://atharayil.medium.com/longest-consecutive-sequence-day-29-python-aa170b1a8cc0
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        count = 0
        longest = 0
        # ? どういうこと？ -> 先頭を外して、c_numsとする
        target = nums.pop(0)
        count = 1
        longest = max(count, longest)
        while nums:
            # この時のnums[0] はpopした後なので、consecutive sequenceになっているのかを確認している
            if target + 1 == nums[0]:
                count += 1
            # 同じ数が連続している場合でもシーケンスにはなるので、その数もスキップする
            # ? けど、set()すればこれもいらなさそう
            # continueで numsのループから抜けて仕切り直す
            elif target == nums[0]:
                nums.pop(0)
                continue
            # それ以外の場合、countをリセットする
            else:
                count = 1
            longest = max(count, longest)
            # ターゲット変更 配列をpopして削ってnumsループを仕切り直す
            target = nums.pop(0)

        return longest
