# @see https://www.interviewbit.com/blog/word-break-problem/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        # init
        dp[0] = True

        for i in range(1, len(s) + 1):
            # ここまでのメモを確認
            for j in range(i):
                # ここまでのメモでtrueかつ、j~iでスライスしたら単語になってたら
                if dp[j] and s[j:i] in wordSet:
                    # dp[i] はokとする
                    dp[i] = True
                    # break loop due to not necessary doing
                    break
        return dp[len(s)]
