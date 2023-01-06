# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # recursiveでやれば結局良さそう　グラフじゃないからな
        # print(root)
        # # res = []
        # if root is None or root.val is None:
        #     return res
        # # 今回も一番下から解決していく
        # if root.left:
        #     left = self.levelOrder(root.left)
        #     print(left)
        #     res.append(left)
        # if root.right:
        #     right = self.levelOrder(root.right)
        #     res.append(right)
        # if root.val:
        #     res.insert(0, [root.val])
        # return res

        # @see https://favtutor.com/blogs/level-order-traversal-python
        # dequeue (double-end queue)で解くらしい。BFSではない？
        res = []
        if root is None:
            return []
        q = collections.deque()
        q.append(root)

        while q:
            curr_size = len(q)
            curr_list = []

            # q.append(root)
            # curr_size = len(q) でやっているから、同じ階層に関して飲みqueueが存在できる
            while curr_size > 0:
                curr_node = q.popleft()
                curr_list.append(curr_node.val)
                curr_size -= 1

                if curr_node.left is not None:
                    q.append(curr_node.left)
                if curr_node.right is not None:
                    q.append(curr_node.right)
            # 同じ階層の要素を上から順にappendする
            res.append(curr_list)
        return res
