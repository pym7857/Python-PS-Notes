n = int(input()) # n = 5

arr = [] 

for _ in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
#print(arr)

# 밑에서 부터 더해서 최대값을 구한다.
# 밑에층의 두개 비교해서, 바로 윗층꺼 숫자를 max값으로 바꾼다.!!
for i in range(n-1, 0, -1): # i = 4,3,2,1 (층수. 맨 윗층 제외) 
    for j in range(i): # j = 0,1,2,3 (해당 층의 index. 마지막 제외)
        temp_max = max(arr[i][j], arr[i][j+1])
        arr[i-1][j] += temp_max

print(arr[0][0])


