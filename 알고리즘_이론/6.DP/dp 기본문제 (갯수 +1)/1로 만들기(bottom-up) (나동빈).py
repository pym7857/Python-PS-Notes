# 1로 만들기 (보텀업)(반복문)

# a(i) = min(a(i-1), a(i//2), a(i//3), a(i//5)) + 1
# 1을 더해주는것은 횟수증가 때문

x = int(input()) # 구하려는 수 : x

dp = [0]*30001

# 1로 만드는게 목표이므로...
# 현재 dp[1] = 0 인 상태
for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 # 1을 뺀 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # 위에서 구한 횟수와 더 작은것 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)
        
print(dp[x])