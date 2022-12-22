class Solution:
    def isValid(self, s: str) -> bool:
        # 左から見ていく
        # 最初に閉じられたのがあったらそこから紐解いていけばいい それが最下層だから
        # 閉じたら、stuckから消していく
        stuck = []
        for i in range(len(s)):
            if len(stuck) > 0 and (
                stuck[-1] + s[i] == "()"
                or stuck[-1] + s[i] == "{}"
                or stuck[-1] + s[i] == "[]"
            ):
                del stuck[-1]
            else:
                stuck.append(s[i])
        return len(stuck) == 0
