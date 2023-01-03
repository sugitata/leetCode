# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursiveにさせて、一番下まで辿り着いたら、そこから解決していって、全部入れ替えていく
        if root is None or root.val is None:
            return None
        else:
            right = self.invertTree(root.left)
            left = self.invertTree(root.right)
            res = TreeNode(root.val, left, right)
            # print(res)
            return res
