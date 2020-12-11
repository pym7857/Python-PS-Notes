# 회의실배정

n = int(input())

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda t: t[0]) # 시작 시간 기준으로 오름차순
arr = sorted(arr, key=lambda t: t[1]) # 종료 시간 기준으로 오름차순

# 1. 이렇게하면, 기존의 시작 시간 기준으로 정렬한 값들을 최대한 유지하려 하기 때문에, 
#       종료 시간이 같다면, 시작 시간이 빠른 기준으로 정렬된 결과가 나타난다. ex.. (1,2), (2,2)
# 2. 종료 시간이 짧은것 먼저 정렬했기 때문에 더 많은 회의들을 추가할 수 있다. 

c = 0
start = 0
for a in arr:
    if a[0] >= start:
        start = a[1]
        c += 1
print(c)


# 입력 예시
'''
11
1 4 
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

# 출력 예시
'''
4
'''