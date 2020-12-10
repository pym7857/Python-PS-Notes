# - 서류 등수 오름차순으로 한번 비교
# - 면접 등수 오름차순으로 한번 비교
# 결과: 시간초과

T = int(input())
for _ in range(T):
    n = int(input())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    arr = sorted(arr, key=lambda t: t[0])
    ans = []
    stand = arr[0]
    if stand not in ans:
        ans.append(stand)

    j = 1
    while j < n:
        if stand[0] < arr[j][0] and stand[1] < arr[j][1]:
            j += 1
        else:
            if arr[j] not in ans:
                ans.append(arr[j])
            stand = arr[j]
            j += 1


    arr = sorted(arr, key=lambda t: t[0])

    stand = arr[0]
    if stand not in ans:
        ans.append(stand)

    j = 1
    while j < n:
        if stand[0] < arr[j][0] and stand[1] < arr[j][1]:
            j += 1
        else:
            if arr[j] not in ans:
                ans.append(arr[j])
            stand = arr[j]
            j += 1

    #print(ans)
    print(len(ans))