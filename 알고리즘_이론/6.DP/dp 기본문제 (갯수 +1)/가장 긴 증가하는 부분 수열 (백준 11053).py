n = int(input())
arr=list(map(int, input().split()))

result = [1] * n
for i in range(1, n):
    for j in range(i): # j=0,1,2,...i-1
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j]+1)

print(max(result))