class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        tmp = strs
        res = []
        while len(tmp) > 0:
            res.append([])
            for i in range(len(tmp) - 1, 0, -1):
                if self.isAnagram(tmp[0], tmp[i]):
                    res[-1].append(tmp[i])
                    # 見つけたやつは消す
                    del tmp[i]
            res[-1].append(tmp[0])
            # 走査してたターゲットは消す
            del tmp[0]
        return res

    def isAnagram(self, a: str, b: str) -> bool:
        tmp_a = a
        if len(a) < 1 or len(b) < 1 or len(a) != len(b):
            return a == b
        for i in range(len(b) - 1, 0, -1):
            foundIndex = tmp_a.find(b[i])
            if foundIndex != -1:
                tmp_a = tmp_a[:foundIndex] + tmp_a[foundIndex + 1 :]
            else:
                return False
        return tmp_a[0] == b[0]
