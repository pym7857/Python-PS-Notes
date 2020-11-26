import sys
sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    
    graph = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    ans = 0
    
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
            
    def dfs(r, c):
        visited[r][c] = True
        
        for dx, dy in directions:
            tr = r + dx
            tc = c + dy
        
            if tr >= 0 and tr < n and tc >= 0 and tc < m:
                if not visited[tr][tc] and graph[tr][tc] == 1:
                    dfs(tr, tc)
                    
            
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                ans += 1
                    
    print(ans)
