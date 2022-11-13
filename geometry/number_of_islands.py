# @see https://leetcode.com/problems/number-of-islands/solutions/56340/Python-Simple-DFS-Solution/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        # ? gridって名前適切なのか？ len(grid)は縦列の長さじゃない？
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    # 再帰探索が終了した時点で、そのi, jと陸続きのところの探索は終わっているので、count++する
                    count += 1
        return count

    def dfs(self, grid: List[List[str]], i: int, j: int):
        # そこを探索するかどうかの判断
        # 今の grid target が 1 (島) じゃなかったら、繋がった島探索は終了
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return

        # 探索し終わったマスは#としておく
        grid[i][j] = "#"
        # そのマスの四方がどうなっているのかを再帰で確認する
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
