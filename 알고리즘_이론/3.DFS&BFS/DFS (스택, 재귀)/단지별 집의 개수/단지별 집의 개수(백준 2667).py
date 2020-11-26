n = int(input())

graph = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]
directions = [(0,1), (0,-1), (1,0), (-1,0)]
res = []
cnt = 0

for i in range(n):
    line = str(input())
    for j, b in enumerate(line):
        graph[i][j] = int(b)
        
def dfs(r, c):
    global cnt
    
    visited[r][c] = True
    
    for dx, dy in directions:
        tr = r + dx
        tc = c + dy
    
        if tr >=0 and tr < n and tc >=0 and tc < n:
            if not visited[tr][tc] and graph[tr][tc] == 1:
                cnt += 1
                dfs(tr, tc)
                
    return cnt
        
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = 1
            res.append(dfs(i, j))
            
#print(res)
print(len(res))
res=sorted(res)
for a in res:
    print(a)