# 출처: https://claude-u.tistory.com/204
# 계단 오르기(2579)랑 똑같은 점화식 아님 !!

n = int(input())

arr = [0] # 인덱스 0 은 자리만 채워주기
for _ in range(n):
    arr.append(int(input()))
dp = [0 for _ in range(n + 1)] # 인덱스 0 은 자리만 채워주기

for i in range(1, n + 1):
    if i == 1:
        dp[1] = arr[1]
    if i == 2:
        dp[2] = arr[1] + arr[2]
    else:
        # 한번에 뛸 수 있는 거리는 무제한! (이게 바로 계단 오르기(2579)와 다른 점 )
        # 연속된 세잔 마실 수 X
        # 포도주의 양은 0일 수 있다.

        # 점화식
        # 1. target이전꺼 안 마시는 경우
        # 2. 연속 두개
        # 3. target을 마시지 않는 경우
        for i in range(3, n+1):
            dp[i] = max(arr[i] + dp[i-2],
                        arr[i] + arr[i-1] + dp[i-3],
                        dp[i-1])

print(dp[n])

# 반례
'''
6
999
999
1
1
999
999

answer: 3996
'''