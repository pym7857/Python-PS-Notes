# 나동빈 p.227
# 화폐들의 개수를 최소한으로 이용해서 합계 금액을 구성

# 예시
# 3 7(가치의 합)
# 2
# 3
# 5

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input())) # arr = [2,3,5]

dp = [10001]*(m + 1)

dp[0] = 0

for i in range(n): # i = 0,1,2
    for j in range(arr[i], m + 1):
        dp[j] = min(dp[j], dp[j - arr[i]] + 1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])