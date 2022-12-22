class Solution:
    def isPalindrome(self, s: str) -> bool:
        # @see https://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python
        s2 = "".join(cha for cha in s if cha.isalnum()).lower()
        size = len(s2)
        for i in range(size // 2):
            print(s2[i])
            print(s2[size - 1 - i])
            if s2[i] != s2[size - 1 - i]:
                return False
        return True
