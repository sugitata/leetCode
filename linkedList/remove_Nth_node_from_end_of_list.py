# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @see https://dev.to/seanpgallivan/solution-remove-nth-node-from-end-of-list-4njl
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        if not fast:
            # ? なんで？ fastがないときにそうなる？
            # ? -> fast.next が None になるときは、 nが len(head) の時
            return head.next
        # fast.nextをさらにループさせて、tailになるまでやる
        # nから余った分だけslowも移動される
        # -> fastはslowのtailを　Nthに持っていくためだけのもの
        while fast.next:
            fast, slow = fast.next, slow.next
        # ? slowのnextは次の次とする
        # -> tailのところが removeする、 Nthの箇所だから
        slow.next = slow.next.next
        # ? なんで最後はheadなんだ？
        # -> slowは保存されている？ fastは保存されてなさそうなのに？
        # ? -> slownとfastの変更でheadに副作用があるのはなぜ？ポインタ参照している？
        return head
