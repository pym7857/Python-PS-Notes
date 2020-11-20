class Solution(object):
    def dfs(self, r, c, grid):
        global visited, rows, cols
        
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        
        if grid[r][c] == "1" and not visited[r][c]:
            visited[r][c] = True
            self.dfs(r-1, c, grid)
            self.dfs(r+1, c, grid)
            self.dfs(r, c-1, grid)
            self.dfs(r, c+1, grid)
        else:
            return
        
    def numIslands(self, grid):
        global visited, rows, cols
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        total = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False]*cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    self.dfs(r, c, grid) # 연관된 것들 방문처리 해주기
                    total += 1
                        
        #print(total)
        return total