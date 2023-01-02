# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # # BFS
        # # @see https://qiita.com/drken/items/996d80bcae64649a6580
        # # dictでやると、同じ数がある場合に詰む
        # seen = {}
        # seen[root.val] = 1
        # q = [root]
        # # dictのkeyをユニークにするため
        # # [0,0,0,0,null,null,0,null,null,null,0] みたいな時に対応するため
        # # length = 0
        # while len(q) > 0:
        #     v = q.pop(0)
        #     # u_key = v.val + seen[v.val]
        #     if seen[]
        #     if v.left is not None:
        #         # keyをユニークにさせる
        #         # value + parentの階層
        #         u_key = v.left.val + seen[v.val]
        #         #
        #         seen[u_key] = seen[v.val + seen[v.val]] + 1
        #         q.append(v.left)
        #     if v.right is not None:
        #         u_key = v.right.val + seen[v.val]
        #         seen[u_key] = seen[v.val] + 1
        #         q.append(v.right)

        # return max(seen.values())

        # @see https://www.educative.io/answers/finding-the-maximum-depth-of-a-binary-tree
        if root is None:
            return 0

        left_d = self.maxDepth(root.left)
        right_d = self.maxDepth(root.right)

        # left_d と right_dの値は常に保存されている
        # left_dとright_dの大きい方どちらかがあれさえばいいので、これでインクリメントしていく
        # 以下が呼ばれるのは、 self.maxDepth()でrecursiveで最下層まで届いてから、ボトムアップでresolveしていく
        if left_d > right_d:
            return left_d + 1
        else:
            return right_d + 1
