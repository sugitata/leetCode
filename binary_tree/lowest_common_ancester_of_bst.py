# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # inOrderで、その二つの要素より前の配列をsliceしてminすれば終わりそう -> だめ
        # order = []

        # def inOrder(root, order):
        #     if not root or root.val is None:
        #         return
        #     inOrder(root.left, order)
        #     order.append(root.val)
        #     inOrder(root.right, order)

        # inOrder(root, order)
        # print(order)
        # i = order.index(p.val)
        # print(i)
        # sliced = order[0 : i + 1]
        # print(sliced)
        # # 返すのは TreeNodeみたい　あと、qはどこで使うんだろうか
        # return min(sliced)

        # @see https://en.wikipedia.org/wiki/Lowest_common_ancestor
        # RMQ(range minimum query) と preOrder で考える
        # preorderでindexを算出して、範囲を決める
        # v: [6, 2, 0, 4, 3, 5, 8, 7, 9] e.g. p=2 q=8
        # i: [0, 1, 2, 3, 4, 5, 6, 7, 8] e.g. range: 1~6
        # d: [0, 1, 2, 2, 3, 3, 1, 2, 2] e.g. 2はd:1, 8はd:1

        # @see https://palashsharma891.medium.com/235-lowest-common-ancestor-of-a-binary-search-tree-leetcode-python-f415d804e91d
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr
