class Solution:
    def numDecodings(self, s: str) -> int:
        # list: s[i]
        # メモするべきもの: その単語の長さまでの組み合わせの数
        # 考慮するべきもの: 0は単体で使用できない（10, 20として使用するしかない）
        arr = list(s)
        if arr[0] == "0":
            return 0
        # そこまでに格納できる組み合わせのtotal
        dp = [0] * (len(arr))
        # init
        dp[0] = 1
        # ! これだとだめ
        for w in range(1, len(arr)):
            # ? 含めていい数字は何か -> 1~26
            # -> つまり、以下の条件なら含める
            # 1. i: 1~9
            # 2. i-1: 1or2 and i: 0~6
            if arr[w - 1] == "1" or arr[w - 1] == "2":
                dp[w] = dp[w - 1] + 2
            else:
                dp[w] = dp[w - 1] + 1
        return dp[-1]

        # @see https://www.tutorialspoint.com/decode-ways-in-python
