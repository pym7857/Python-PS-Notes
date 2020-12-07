n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# dp배열도 arr과 같은 형태가 되어야 한다.
dp = [[-1]*3 for _ in range(n)] # RGB 집 이므로, 가로 길이 = 3

# dp시작
# 모든 집을 칠하는 비용의 최솟값을 출력한다.
# 맨 윗 숫자 (start) 를 기준으로 내려가기...
dp[0][0] = arr[0][0]
dp[0][1] = arr[0][1]
dp[0][2] = arr[0][2]

for i in range(1, n): # 2번째 줄 부터...
    # R
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    # G
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    # B
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

min_val = min(dp[-1][0], dp[-1][1], dp[-1][2])
print(min_val)

