# @see https://python.plainenglish.io/leet-code-191-number-of-1-bits-explained-python3-solution-661a2b77e8c3
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while True:
            if n == 0:
                break
            if n & 1 == 1:
                count += 1
            n = int(n / 2)
        return count
