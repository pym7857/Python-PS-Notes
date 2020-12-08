# 출처: https://sungmin-joo.tistory.com/18

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
#print(arr) # [10,20,15,25,10,20]

dp = [0]*n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
elif n == 3:
    print(max(arr[0] + arr[2], arr[1] + arr[2]))
else:
    # 계단은 한 칸 혹은 두 칸씩 오를 수 있다.
    # 연속된 세 개의 계단을 모두 밟아서는 안 된다.
    # 마지막 도착 계단은 반드시 밟아야 한다.
    # max(바로전꺼 안 밟았던 경우, 바로전꺼 밟았던 경우)

    # 역으로 할 필요가 없다.
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, n):
        dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3]) # 점화식
    #print(dp)

    print(dp[-1])

