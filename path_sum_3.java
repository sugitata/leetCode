/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pathSum(TreeNode root, int sum) {
        if (root == null) return 0;
        return findPath(root, sum) + pathSum(root.left, sum) + pathSum(root.right, sum); 
    }

    private int findPath(TreeNode node, int sum) {
        int res = 0;
        if (node == null) return res;
        // 設定している合計値がnode.valと一致していたら今のDFTに値をインクリメントする
        if (node.val == sum) res++;

        // 今の値分は引いて、それをsumとして次のnode.valと一致するのかを確かめる
        res += findPath(node.left, sum-node.val);
        res += findPath(node.right, sum-node.val);
        return res;
    }
}
