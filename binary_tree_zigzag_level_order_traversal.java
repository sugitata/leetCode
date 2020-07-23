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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;
        Queue<TreeNode> queue = new LinkedList();
        // offerは例外を返さずfalseを返す
        queue.offer(root);
        boolean zigzag = false;
        while(!queue.isEmpty()) {
            List<Integer> currLevel = new ArrayList<>();
            int size = queue.size();
            // for文にqueue.size()を含めてしまうと、内部でqueueを変化させてるので先にsizeを定義しておかないといけない
            for(int i = 0; i < size; i++) {
                // pollは削除して取り出す
                TreeNode node = queue.poll();
                if(zigzag) {
                    // 先頭に追加
                    currLevel.add(0, node.val);
                } else {
                    currLevel.add(node.val);
                }
                if(node.left != null) {
                    queue.add(node.left);
                }
                if(node.right != null) {
                    queue.add(node.right);
                }
            }
            res.add(currLevel);
            zigzag = !zigzag;
        }
        return res;
    }
}
