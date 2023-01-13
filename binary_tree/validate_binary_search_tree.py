# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 探索木なので left.val < root.val < right.val になっていることが条件
        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return True

        # l = True
        # r = True
        # if root.left:
        #     if root.val > root.left.val:
        #         l = self.isValidBST(root.left)
        #         # print(l)
        #     else:
        #         return False
        # if root.right:
        #     if root.val < root.right.val:
        #         r = self.isValidBST(root.right)
        #         # print(r)
        #     else:
        #         return False
        # if not l or not r:
        #     return False

        # return True
        # # これで解こうとすると、孫の木の同じ階層の要素も潤になっていることが検証できない...
        # # e.g. [5,4,6,null,null,3,7] -> expected: false ( 3 が 6 の childNode だから)

        # @see https://zhenyu0519.github.io/2020/03/09/lc98/
        if not root:
            return True

        # https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
        # 1. inOrder traversal で配列に格納していく
        # 2. 順番が正しくなかったら、BSTの条件に反するので、return Falseすればいいだけ
        order = []

        # helper
        def inOrder(root, order):
            if root is None:
                return
            inOrder(root.left, order)
            order.append(root.val)
            inOrder(root.right, order)

        inOrder(root, order)
        for i in range(1, len(order)):
            if order[i] <= order[i - 1]:
                return False
        return True
