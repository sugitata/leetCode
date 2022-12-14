class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # # これもmaxとかでやった方が良さそう
        # # seen = {}
        # start = 0
        # max_length = 0
        # tmp_k = k
        # # 1. kでどれぐらい変えられるかをstartからendまで確認する
        # # 2. maxをとっていく
        # for end in range(len(s)):
        #     # 同じletterじゃないなら
        #     # print(end)
        #     if s[start] != s[end]:
        #         tmp_k -= 1
        #     # end + 1 < len(s) : 最後の要素の一個手前まで
        #     # s[start] == s[end + 1] : 次の要素が同じ文字か
        #     # AABA start: 1, end: 2
        #     # これだと s[end + 1]がAだからスキップされてしまう
        #     # endが次に3になってしまうから良くない
        #     if end + 1 <= len(s) - 1 and s[start] == s[end + 1]:
        #         print("skip")
        #         continue
        #     if tmp_k <= 0:
        #         print(start)
        #         print(end)
        #         max_length = max(max_length, end - start + 1)
        #         print(max_length)
        #         start = end
        #         # リセット
        #         tmp_k = k
        #     elif end + 1 == len(s):
        #         max_length = end - start + 1
        # return max_length

        # @see https://palashsharma891.medium.com/424-longest-repeating-character-replacement-leetcode-python-906d6b0e357c
        seen = {}
        max_length = 0
        start = 0
        for end in range(len(s)):
            # ? dict.get()ってどう言うこと？
            # -> s[end] のkeyの値を取る。　default は 0 として fallback
            seen[s[end]] = 1 + seen.get(s[end], 0)

            # dict.values() で Iterative を出力できる。 max() は Iterative を引数に取れる
            # O(n^2)で endは固定 endからスタートまでの差において
            # -> endが固定なので、そのendの値に対して A, Bお互いをseen(DP)で競わせる感じ
            # seen[s[start]] 例えば Aのvalueをどんどん小さくしていく
            while (end - start + 1) > max(seen.values()) + k:
                seen[s[start]] -= 1
                start += 1

            max_length = max(end - start + 1, max_length)

        return max_length
