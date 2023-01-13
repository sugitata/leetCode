# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
        # 1. inOrder traversal で配列に格納していく
        # 2. 順番が正しくなかったら、BSTの条件に反するので、return Falseすればいいだけ
        def inOrder(root, order):
            # if not root.val にすると、`0` も False 扱いになるので注意
            if root is None or root.val is None:
                return
            inOrder(root.left, order)
            order.append(root.val)
            inOrder(root.right, order)

        inOrder(root, order)
        # print(order)

        return order[k - 1]
