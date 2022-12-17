class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = t
        if len(s) == 1 or len(s) != len(t):
            return s == t
        for i in range(len(t) - 1, 0, -1):
            foundIndex = tmp.find(s[i])
            if foundIndex != -1:
                # 見つけたインデックスを除いたtmp_tにする
                tmp = tmp[:foundIndex] + tmp[foundIndex + 1 :]
            else:
                return False
        return tmp[0] == s[0]
