# 아이디어:
# '-'로 일단 나누고 (split)
# 나눠진것 각각에서 '+'로 또 나눠서 그 더한값을 저장한다.

# 55-(50+40)
# (55+50)-40
# 55-50-40-30
# 55-(50+40)-30
# 55-(50+40+30)

s = str(input())

s = s.split('-')
#print(s)

ans = 0
if len(s[0]) == 2:
    ans = int(s[0])
else:
    c = s[0].split('+')
    temp = 0
    for d in c:
        temp += int(d)
    ans = temp

for a in s[1:]:
    a = a.split('+')
    #print(a)
    temp = 0
    for b in a:
        temp += int(b)
    #print(temp)
    ans -= temp
print(ans)