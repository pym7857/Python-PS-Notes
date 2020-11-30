from collections import deque

n, m = map(int, input().split()) # 가로, 세로

graph = []
for _ in range(m):
    lst = list(map(int, input().split()))
    graph.append(lst)
#print(graph)

visited = [[False]*n for _ in range(m)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]

start = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            start.append((i, j))
#print(start)

q = deque(start) # q = [(0,0), (3,5)]
    
cnt = 0
while q:
    
    cnt += 1
    next = [] # 다음 턴에 작업할 좌표들 
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in directions:
            tx = x + dx
            ty = y + dy
            
            if 0<= tx < m and 0 <= ty < n and not visited[tx][ty] and graph[tx][ty] == 0:
                visited[tx][ty] = True
                graph[tx][ty] = 1
                next.append((tx, ty))
                
    #print(next)
    q = deque(next)
    
# 0인게 있으면 -1을 출력
flag = False

for a in graph:
    for b in a:
        if b == 0:
            flag = True
            
if flag:
    print(-1)
else:
    print(cnt-1)