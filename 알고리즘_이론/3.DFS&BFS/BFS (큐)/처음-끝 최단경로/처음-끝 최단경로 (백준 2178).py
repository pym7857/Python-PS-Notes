from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    lst = list(str(input()))
    lst = list(map(int, lst))
    graph.append(lst)
#print(graph)

visited = [[False]*m for _ in range(n)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]
dist = [[0]*m for _ in range(n)] # 거리 기록
dist[0][0] = 1

def bfs(r, c):
    global visited
    
    visited[r][c] = True
    q = deque([(r, c)])
    
    while q:
        cur_x, cur_y = q.popleft()
        
        for dx, dy in directions:
            tx = cur_x + dx
            ty = cur_y + dy
            
            if 0 <= tx < n and 0 <= ty < m:
                if graph[tx][ty] == 1 and not visited[tx][ty]:
                    visited[tx][ty] = True
                    q.append((tx, ty))
                    dist[tx][ty] = dist[cur_x][cur_y] + 1
                    
bfs(0, 0)

print(dist[-1][-1])