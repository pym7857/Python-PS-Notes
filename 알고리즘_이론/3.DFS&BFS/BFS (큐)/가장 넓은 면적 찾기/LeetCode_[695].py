# 1로 이루어진 / 면적 제일 넓은 / island 의 면적 찾기 -> BFS

import sys
from collections import deque

class Solution(object):
    def __init__(self):
        self.directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    def bfs(self, grid, r, c):
        global visited
        
        temp_sum = 1
        visited[r][c] = True
        queue = deque([(r, c)])
        
        while queue:
            cur_x, cur_y = queue.popleft() 
            for dx, dy in self.directions: # 동서남북
                tx = cur_x + dx
                ty = cur_y + dy
                if tx < 0 or tx >= len(grid) or ty < 0 or ty >= len(grid[0]): # 범위에서 벗어나는지
                    continue    # 다음 for문으로 넘기기
                if grid[tx][ty] == 1 and not visited[tx][ty]:
                    visited[tx][ty] = True
                    queue.append((tx, ty))
                    temp_sum += 1
        return temp_sum
            
    
    def maxAreaOfIsland(self, grid):
        global visited
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        visited = [[False]*cols for _ in range(rows)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    res = max(res, self.bfs(grid, r, c))
        
        return res