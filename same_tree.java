class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // if both of them are null
        if (p == null && q == null) return true;
        // if either of them is null
        if (p == null || q == null) return false;

        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}