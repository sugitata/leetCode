class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 現在のindex番号から、valueの値を使ってその分ジャンプできる
        # そのジャンプで最後まで辿り着けるか？というゲーム

        # @see https://github.com/zhouchong90/LeetCode-Python-Solution/blob/master/Solutions/55%20Jump%20Game.py
        # can_jampの場合は、メモをして行って、0になったらfalseを返す

        # @see https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)
        lastPosition = len(nums) - 1

        # e.g. [2, 3, 1, 1, 4] => True
        # e.g. [3, 2, 1, 0, 4] => False
        for i in range(len(nums) - 2, -1, -1):  # loop to backwards
            # ターゲットの数字(後ろから順に)とindex足し合わせて、それが最後のインデックスより大きいなら
            # ? -> つまりどういうこと
            # i: ジャンプするposition
            # nums[i]: ジャンプできるstep数
            # -> これらを足し合わせてlas positionに届くのかを判定している
            # -> かつ、そのposiitonに届くのなら、lastPositionを手前に戻す
            # -> そして無事にindex: 0まで辿り着けるのなら、canJump: Trueということになる
            if (i + nums[i]) >= lastPosition:
                lastPosition = i
        return lastPosition == 0
