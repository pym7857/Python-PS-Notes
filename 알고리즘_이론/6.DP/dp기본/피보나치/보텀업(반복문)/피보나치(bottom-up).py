# 피보나치 수열 (보텀업)(반복문)
# 1, 1, 2, 3, 5, 8, 13

dp = [0]*101

dp[1] = 1
dp[2] = 1
n = 7

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
    
print(dp[n])