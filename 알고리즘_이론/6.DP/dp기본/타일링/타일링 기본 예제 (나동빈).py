# 문제 (나동빈 p.224)
# 2x1, 1x2, 2x2 타일 보유

n = int(input())

dp = [0]*1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = d[i-1] + 2*d[i-2]
