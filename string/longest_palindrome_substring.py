class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = s[0]
        for i in range(len(s)):
            if len(res) < len(s[i:]):
                subSize = self.maxPalindrome(s[i:])
            if len(res) < subSize:
                res = s[i:][0:subSize]
        return res

    def maxPalindrome(self, s: str) -> int:
        stuck = []
        size = 1
        for i in range(len(s)):
            # 隣り合った数が同じ時
            # e.g. aa
            # これだと cccみたいなのに対応できない　　ccで処理されてしまう
            if len(stuck) > 0 and stuck[-1] == s[i]:
                del stuck[-1]
                size += 1
            # e.g. bab (stuck: ['b'], s[i]: a, s[i+1]: b)
            elif len(stuck) > 0 and i + 1 < len(s):
                if stuck[-1] == s[i + 1]:
                    # e.g. aはstuckもしないので、無視
                    size += 1
            else:
                stuck.append(s[i])
        print("size返します")
        print(size)
        return size
