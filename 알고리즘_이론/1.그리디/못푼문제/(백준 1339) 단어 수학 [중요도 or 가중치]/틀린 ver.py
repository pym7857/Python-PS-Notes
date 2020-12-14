# 앞자리부터 9넣으면 되는 줄 알았다...
# 반례가 있다... (맨 밑)

n = int(input())
arr = []
max_len = 0
for _ in range(n):
    lst = list(str(input()))
    if max_len < len(lst):
        max_len = len(lst)
    arr.append(lst)

# 0 채워주기
for i in range(len(arr)):
    if len(arr[i]) < max_len:
        arr[i] = ['0']*(max_len - len(arr[i])) + arr[i]

#print(arr)

dic = dict()

# 9,8,7,,,1,0 채워주기

num = 9
for i in range(max_len): # 자리수
    for j in range(len(arr)):
        if arr[j][i] != '0':
            if arr[j][i] not in dic:
                dic[arr[j][i]] = num
                arr[j][i] = str(num)
                num -= 1
            else:
                arr[j][i] = str(dic[arr[j][i]])
print(dic)
#print(arr)

total = 0
for a in arr:
    total += int(''.join(a))
print(total)


# 아마 틀린 케이스는

# 10
# ABB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB

# 이거 알맞게 나오나요? B가 9, A가 8들어가야 합니다.