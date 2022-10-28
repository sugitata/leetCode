# Definition for a Node.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# @see https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/clone-graph.py
# deep cloneせよ、という問題
class Solution:
    # def cloneGraph(self, node: Node) -> Node:
    def cloneGraph(self, node: Node) -> Node:
        if node is None:
            return None
        clonedNode = Node(node.val)
        # ? clonedの型がいまいちわからない
        cloned, queue = {node: clonedNode}, [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                # clonedの中にまだ neighbor として持っているものが追加されてなかったら
                # 1. まだ確認してなさそうなので、queueに追加する
                # 2. neighborをちゃんとNode型にして、clonedに追加する
                if neighbor not in cloned:
                    queue.append(neighbor)
                    # ? cloned neighborを新しく作る
                    clonedNeighbor = Node(neighbor.val)
                    # cloned(result)のneighborの位置に clonedを追加
                    # ? neighborってNode型なのにindexあるの？？
                    # -> どうやらkeyで持たせている　オブジェクト(連想配列)みたい
                    cloned[neighbor] = clonedNeighbor
                # 今確認中の queueのNodeに、neighborsとして今回cloneしたneighborを追加する
                # -> clonedにはもう追加されているので、次回のチェックは不要となる
                cloned[current].neighbors.append(cloned[neighbor])
        # ? 最後はclonedではなく、 cloned[node]を返すのか
        return cloned[node]
