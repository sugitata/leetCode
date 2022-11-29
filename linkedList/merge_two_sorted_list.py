# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @see https://qiita.com/KueharX/items/7112e8bd9dbf69f5c083
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp = ans = ListNode(0)
        while list1 and list2:
            # list2 が大きいなら、小さい順に並んでいるのでans.nextにはlist1を追加する
            if list1.val < list2.val:
                ans.next = list1
                # list1は評価し終わったので、next
                list1 = list1.next
            else:
                ans.next = list2
                list2 = list2.next
            # ansは評価し終わったので、次はans.nextに何を詰め込むかを考える
            ans = ans.next
        # ? ans.nextは最終的に list1 or list2で orをとる なんで？
        # -> list1 and list2でどっちかがなくなったらwhile loopは終わる
        # -> 残ったほうはあとは追加するだけでいいので、 ans.nextに最後その余り物を追加して終わり
        ans.next = list1 or list2
        return temp.next
