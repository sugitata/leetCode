/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        Stack<Node> stack = new Stack<>();

        Node node = head;
        Node next = null;

        // nodeがnullになるまで探索を繰り返す
        while(node != null) {
            // nodeにchildがいた場合、childをnextに置き換えて、childを削除してflatten。元のnextはstackに避難させる
            if (node.child != null) {
                if (node.next != null) {
                    next = node.next;
                    next.prev = null;
                    stack.push(node.next);
                }
                next = node.child;
                node.next = next;
                next.prev = node;
                node.child = null;
            }
            // nodeにchildがいなくて、nextが尽きた場合、stackに避難させたnextが残っていたら１個上の階層に戻る
            if (node.next == null && stack.size() > 0) {
                next = stack.pop();
                node.next = next;
                // prevも定義しないといけない　双方向リストだから
                next.prev = node;
            }
            // 次のnodeに移行するため node = node.nextにして次のloopへ
            node = node.next;
        }

        // nodeはcurrとして扱っているものだから、これをreturnさせても最後はnode!=nullで終了するので意味ない
        // return node;
        // headの値が変わるのは、nodeがheadのオブジェクトを参照しているから？
        return head;
    }
}