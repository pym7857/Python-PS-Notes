# 아이디어: https://dev-wd.github.io/algorithm/backjoon10844/

n = int(input())

dp = [1]*10 # 1의자리: 0, 1, 2, ... 9

if n == 1:
    print(sum(dp[1:]))
else:
    for _ in range(n-1):
        new = [0]*10
        new[0] = dp[1]
        new[9] = dp[8]
        for i in range(1, 9): # i = 1,2,...8
            new[i] = dp[i-1] + dp[i+1]
        dp = new
     
    print(sum(dp[1:])%1000000000)



