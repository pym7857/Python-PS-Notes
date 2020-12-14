# https://it-garden.tistory.com/89
# 아이디어:
# 키큰 사람부터 자리에 넣으면서, 다음 키작은 사람이 그 위치면 밀어내기(=insert()사용)

n = int(input())
arr = input().split()
arr = list(map(int, arr))

res = list()
for i in range(n):
    res.insert(arr[n-1-i], n-i) # insert(): 밀어내기 가능

print(*res)

# 입력 예시
'''
4
2 1 1 0
'''
# arr[4]이면, res[0]자리에 4를 넣기
# arr[3]이면, res[1]자리에 3을 넣기
# arr[2]이면, res[1]자리에 2를 넣는데, res[1]자리에 값이 있다면, 뒤로 밀어내기
# arr[3]이면, res[2]자리에 1을 넣는데, res[2]자리에 값이 있다면, 뒤로 밀어내기