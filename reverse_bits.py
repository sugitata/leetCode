# @see https://medium.com/@nkwade/leetcode-190-reverse-bits-python-solution-464771568ffe
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))
        return res
