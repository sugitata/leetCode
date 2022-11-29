# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @see https://medium.com/@ektadhobley/reorder-list-leetcode-medium-blind-75-linked-list-391f46780904
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # L0 -> Ln -> L1 -> L(n-1) -> L2 -> L(n-2) みたいに入れ替える
        # [1,2,3,4]
        # slow: [1,2,3,4]
        slow = head
        # fast: [2,3,4]
        # head.nextにしておくのは、[2]からslowはスタートしたいから
        fast = head.next

        # いつものfastの分だけ最初にずらす戦法
        # fast.next.nextで１step skipするので、[1, 2, 3, 4] -> [2, 4] みたいになる
        while fast and fast.next:
            slow = slow.next
            # fastの役割はここで終わり
            # slowの位置をずらすだけ
            fast = fast.next.next

        # ? ここが一番よくわからない
        # e.g. second = [2,3,4]
        # head of second list
        second = slow.next  # second: [3, 4]
        # pointing tail of first list to null
        # ここでslowの役目は終了　あとはsecond
        slow.next = None  # slow: [2]
        # prevとは？
        prev = None

        # headがこの段階で [1,2,3,4]から[1,2]になる
        # slow: [2,3,4] で、　slow.next = None にしたから
        # 🔵 使い終わった slowをわざわざNoneにしているのは、headをいじるためだったんだ１

        # reverse
        # second.nextを退避させて入れ換えている [3, 4] => [4, 3] になる
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halves (half)
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
