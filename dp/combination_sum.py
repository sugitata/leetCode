class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp = [0] * len(nums) + 1
        # weight: target
        # e.g. target = 4 の時 1~4までの組み合わせをメモしてゆく
        dp = [0] * (target + 1)
        # init
        # 0の組み合わせはもちろん1通り(何も選択しない)
        dp[0] = 1
        for i in range(1, target + 1):
            for n in nums:
                # 現在考えている `weight` が今組み合わせに入れるか悩んでいる `value` を格納しても溢れないなら
                # ? ピッタリにしなくていいのはなぜなの？(n == iじゃない理由)
                if n <= i:
                    # 組み合わせを加えていく 溢れないnumsの範囲の分だけ
                    dp[i] = dp[i] + dp[i - n]
        return dp[target]
