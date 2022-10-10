# @see https://medium.com/@edward.zhou/leet-code-338-counting-bits-explained-python3-solution-cda868e37d15
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0]

        for i in range(1, n + 1):
            result.append(result[i & (i - 1)] + 1)
        return result
