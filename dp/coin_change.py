class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    # 典型的なナップサックの形 amount: weight で、これを上回らないようにする
                    res[i] = min(res[i], res[i - c] + 1)
        if res[amount] == amount + 1:
            return -1
        return res[amount]
