# @see https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        # preにheadをstash
        # 1の次に2がなくなるまで、ループ後でさせる
        pre = head
        # iterator
        # pre の次の Node がなくなるまで
        while pre.next:
            # next を変数に stash
            nxt = pre.next
            # pre.next を 次の次の要素に入れ替える
            pre.next = nxt.next
            # 次の次は head　にしておく
            # ? なんで？？？
            # ! -> 今の head はnextだから
            nxt.next = head
            # head は nxt つまり pre.next のものに変更
            # next.nextを入れ替えていたので、headはnextになる
            # ? preはどこいった？
            # -> preはnextしかいじらないんだ　それで1の次に2がなくなるまで再帰させている
            head = nxt
        return head
