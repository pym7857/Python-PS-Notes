# https://m.blog.naver.com/pjok1122/221652193756
# https://coreenee.github.io/2020/07/03/%EB%B0%B1%EC%A4%801080(%ED%96%89%EB%A0%AC)/
# 아이디어:
# 왼쪽 위 부터 정답행렬과 숫자가 다르다면, 3*3 뒤집어 나간다.

n, m = map(int, input().split())

arr1 = [list(map(int, input())) for _ in range(n)]
#print(arr1)

arr2 = [list(map(int, input())) for _ in range(n)]
#print(arr2)

def flip(i, j, arr1):
    if i+2 >= n or j+2 >=m: # 3*3 행렬 이므로
        return

    for k in range(i, i+3):
        for l in range(j, j+3):
            if k>=0 and k<n and l>=0 and l<m:
                if arr1[k][l] == 1:
                    arr1[k][l] = 0
                else:
                    arr1[k][l] = 1

c = 0
for i in range(n):
    for j in range(m):
        if arr1[i][j] != arr2[i][j]: # 같지 않다면, 뒤집기
            flip(i, j, arr1)
            #print(arr1)
            c += 1

#print(arr1, arr2)
if arr1 == arr2:
    print(c)
else:  
    print(-1)