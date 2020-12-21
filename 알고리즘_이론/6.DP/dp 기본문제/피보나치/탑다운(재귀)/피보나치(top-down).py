# 피보나치 수열 (탑다운)(재귀)
# 1, 1, 2, 3, 5, 8, 13

dp = [0]*101

def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]
        
print(fibo(7))