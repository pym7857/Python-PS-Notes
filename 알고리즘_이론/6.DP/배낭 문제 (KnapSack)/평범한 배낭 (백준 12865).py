# 개념 설명 : https://claude-u.tistory.com/208
# 문제 풀이 : https://suri78.tistory.com/2

def knapsack(K, wt, v, N): # K: 무게한도, wt: 각 보석의 무게, v: 각 보석의 가치, n: 보석의 개수
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)] # DP를 위한 2차원 리스트
    for i in range(1, N+1):
        for w in range(1, K+1):
            if wt[i] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(v[i] + dp[i-1][w-wt[i]], dp[i-1][w])
    return dp[N][K]

n, k = map(int, input().split())

wt = [0]
v = [0]
for _ in range(n):
    a, b = map(int, input().split()) # 무게, 가치
    wt.append(a)
    v.append(b)

print(knapsack(k, wt, v, n))


