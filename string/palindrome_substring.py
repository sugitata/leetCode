class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for start in range(len(s)):
            count += 1
            for end in range(start + 1, len(s)):
                target = s[start : end + 1]
                if self.isPalindrome(target):
                    count += 1
        return count

    def isPalindrome(self, target: str) -> bool:
        size = len(target)
        if size == 2 and target[0] != target[1]:
            return False
        for i in range(size // 2):
            if target[i] != target[size - 1 - i]:
                return False
        return True
