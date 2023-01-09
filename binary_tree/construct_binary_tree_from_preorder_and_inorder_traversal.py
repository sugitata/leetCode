# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # inorder preorderのtraversalの例
        # @see https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

        # @see https://dev.to/seanpgallivan/solution-construct-binary-tree-from-preorder-and-inorder-traversal-32c5
        m = {inorder[i]: i for i in range(len(inorder))}
        return self.splitTree(preorder, m, 0, 0, len(preorder) - 1)

    def splitTree(
        self, p: List[int], m: dict, pix: int, ileft: int, iright: int
    ) -> TreeNode:
        root_val = p[pix]
        root, imid = TreeNode(root_val), m[root_val]
        if imid > ileft:
            root.left = self.splitTree(p, m, pix + 1, ileft, imid - 1)
        if imid < iright:
            root.right = self.splitTree(p, m, pix + imid - ileft + 1, imid + 1, iright)
        return root
