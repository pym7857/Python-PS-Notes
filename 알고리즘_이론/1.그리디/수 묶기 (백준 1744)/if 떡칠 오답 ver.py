# (음수, 0)을 묶는다
# 왼쪽 끝에서부터 음수를 묶는다
# 오른쪽 끝에서부터 양수를 묶는다

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

total = 0

# 왼쪽 부터 묶기
i = 0
flag1 = False
flag2 = False
flag3 = False # 0이 애초에 없는 경우 
flag4 = False # 0이 맨 처음인 경우

try:
    arr.index(0)
except:
    flag3 = True
if flag3 == False:
    if arr[0] == 0:
        flag4 = True
    else:
        while True:
            total += arr[i] * arr[i+1]
            if arr[i+2] == 0: # 0이 포함 안 되는 경우
                flag1 = True
                break
            if arr[i+1] == 0: # 0이 포함 되는 경우 
                flag2 = True
                break
            i += 2

print(total, flag1, flag2, flag3, flag4)

if flag1:
    arr = arr[i+3:]
    #print(arr) # [3, 6]

    i = len(arr)-1
    while True:
        if i < 0:
            break
        if i - 1 < 0:
            total += arr[i]
            break
        total += arr[i] * arr[i-1]
        i -= 2
    
elif flag2:
    arr = arr[i+2:]
    #print(arr) 

    i = len(arr)-1
    while True:
        if i < 0:
            break
        if i - 1 < 0:
            total += arr[i]
            break
        total += arr[i] * arr[i-1]
        i -= 2
        
elif flag3:
    #print('0없음')
    arr = arr[i+1:]
    #print(arr) # [1,2,3]

    i = len(arr)-1
    while True:
        if i < 0:
            break
        if i - 1 < 0:
            total += arr[i]
            break
        total += arr[i] * arr[i-1]
        i -= 2
    
elif flag4: # 0이 맨 처음인 경우
    arr = arr[1:]

    i = len(arr)-1
    while True:
        if i < 0:
            break
        if i - 1 < 0:
            total += arr[i]
            break
        total += arr[i] * arr[i-1]
        i -= 2

    

print(total)