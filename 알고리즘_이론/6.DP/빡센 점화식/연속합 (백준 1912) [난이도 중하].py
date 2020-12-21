# 점화식 출처: https://claude-u.tistory.com/175

n = int(input())
arr = list(map(int, input().split()))
temp = [0 for _ in range(n)]
result = -1001

for i in range(n):
    temp[i] = max(temp[i-1] + arr[i], arr[i])
    print(i, temp[i])
    result = max(result, temp[i])
    
print(result)