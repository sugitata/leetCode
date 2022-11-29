# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # シンプルに linkedListのtailにポインタが付いてて、そこのindexに値がちゃんと存在しているのか？という問題
    # @see https://zhenyu0519.github.io/2020/06/07/lc141/
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # ? fast, slowってなんでこんな名前なんだ？
        # head, head nodeをとりあえずどちらにもぶち込む
        fast, slow = head, head
        # ? fast と fast.nextがあるかぎり
        # -> これがあるなら、fast.next.nextが None にはなるが、比較はできるから
        while fast and fast.next:
            # ? fast は なぜ次の次に？
            # ? slow は 次だから、slowなのかな？
            fast, slow = fast.next.next, slow.next
            # ? 次の次 と 次が同じとは？
            # -> fastは一個飛ばしで繰り返してて、最後はslowの方に追いつく
            # -> slow に追いつくってことは、循環しているってことの照明になる
            # -> 逆に循環してなかったら、 fast, fast.nextが存在しないってことになる
            # ? fast.nextが消える時ってあるのかな？ -> ある
            if fast == slow:
                return True
        return False
