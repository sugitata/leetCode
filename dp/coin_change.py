class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # e.g. [0, 12, ..., 12] (len: 12) の配列用意 (amount: 11)
        # 12を格納しているのは、コインを投げる回数としてあり得ない数値だから
        res = [amount + 1] * (amount + 1)
        res[0] = 0
        # 典型的なナップサックの形 amount: weight で、これを上回らないようにする
        # i: メモしていきたいweight max
        for i in range(1, amount + 1):
            # c: 組み合わせを考えていくコインのweight
            for c in coins:
                # Weigh maxを今回のコインが超えてなければ、入れる考慮をする余地あり
                # それ以外の場合はスキップ
                if i >= c:
                    # 初期値は12であり、それとメモしてた回数+今回のコインで(res[i-c]+1)で比較
                    # 基本的には12が削除される
                    res[i] = min(res[i], res[i - c] + 1)
        # res[11](今回求めたい、メモの到達点である最大値)の回数がそもそも 11を超えて12のままなら、それはあり得ないので-1
        if res[amount] == amount + 1:
            return -1
        return res[amount]
