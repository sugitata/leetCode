# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # print(p)
        # print(q)
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            right = self.isSameTree(p.right, q.right)
            left = self.isSameTree(p.left, q.left)
            if right and left:
                return True
        else:
            return False
