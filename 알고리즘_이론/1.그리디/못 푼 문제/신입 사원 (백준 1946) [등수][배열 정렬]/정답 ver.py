# 서류점수 기준으로 오름차순 한 다음,
# 서류점수 1등인 사람의 면접 점수를 min값으로 시작하여 풀이

# pypy로 실행해야 정답 처리받음

T = int(input())
for _ in range(T):
    n = int(input())

    arr = [0] * (n + 1)
    
    for _ in range(n):
        a, b = map(int, input().split())
        arr[a] = b

    min_val = arr[1] # 서류 1등인 사람의 면접 등수    
    
    c = 1
    for i in range(2, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            c += 1

    print(c)
    