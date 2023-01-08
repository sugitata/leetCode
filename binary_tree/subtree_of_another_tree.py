# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # queueでやれば良さそう
        # if root is None:
        #     return False
        # # res = False
        # q = collections.deque()
        # q.append(root)

        # while q:
        #     curr = q.popleft()
        #     print(curr.left)
        #     print(curr.right)
        #     if curr.val == subRoot.val and curr.left and curr.right:
        #         # これでやっても、1階層のsubtreeの一致しか確かめられない
        #         # TODO おそらく、root.valが一致していたら、そこからまたwhileループする必要がある
        #         if (
        #             curr.left.val == subRoot.left.val
        #             and curr.right.val == subRoot.right.val
        #             and curr.left.right is None
        #             and curr.left.left is None
        #             and curr.right.left is None
        #             and curr.right.right is None
        #         ):
        #             return True
        #     if curr.left is not None:
        #         q.append(curr.left)
        #     if curr.right is not None:
        #         q.append(curr.right)
        # return False

        # @see https://palashsharma891.medium.com/572-subtree-of-another-tree-leetcode-python-368d61116758
        if not subRoot:
            return True
        if not root:
            return False
        if self.identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def identical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.identical(p.left, q.left) and self.identical(p.right, q.right)
