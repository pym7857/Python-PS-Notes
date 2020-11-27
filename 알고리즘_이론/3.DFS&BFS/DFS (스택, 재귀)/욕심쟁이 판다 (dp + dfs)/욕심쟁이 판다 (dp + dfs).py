import sys
sys.setrecursionlimit(10**8)

def dfs(r, c):
    if memo[r][c]:
        return memo[r][c]
        
    memo[r][c] = 1
    
    for dx, dy in directions:
        tr = r + dx
        tc = c + dy
        
        if 0 <= tr < n and 0 <= tc < n and graph[r][c] < graph[tr][tc]:
            memo[r][c] = max(memo[r][c], dfs(tr, tc) + 1) # 점화식에 1을 더해주는 이유는 함수의 호출횟수 1을 더한것
        
    return memo[r][c]
    
    
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
memo = [[0]*n for _ in range(n)]
directions = [(0,1),(0,-1),(1,0),(-1,0)]

for i in range(n):
    for j in range(n):
        memo[i][j] = dfs(i, j)
        #print(memo)
        
print(max(map(max, memo))) # 2차원배열에서 가장 큰 수 구하는 방법