# https://suri78.tistory.com/149
# 아이디어:
# (음수, 0)
# (음수, 음수)
# (양수, 양수)
# (1, 양수) ... X

# 음수, 양수 나눠서 입력받기 (핵심)

n = int(input())
neg = []
pos = []
for _ in range(n):
    num = int(input())
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

neg = sorted(neg) # [-5, -4, -3, ...0]
pos = sorted(pos, reverse=True) # [5, 4, 3, ... 1]

total = 0
for i in range(0, len(neg), 2):
    if i == len(neg)-1:
        total += neg[-1]
    else:
        total += neg[i]*neg[i+1]
#print(total)

for i in range(0, len(pos), 2):
    if i == len(pos)-1:
        total += pos[-1]
    elif pos[i+1] != 1:
        total += pos[i]*pos[i+1]
    elif pos[i+1] == 1:
        total += pos[i] + 1
print(total)