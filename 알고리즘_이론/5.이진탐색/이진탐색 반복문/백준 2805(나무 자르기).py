n, m = map(int, input().split())

arr = list(map(int, input().split()))

low = 0 # 시작점 = 0
high = max(arr)

result = 0
while(low<=high):
    mid = (low+high)//2
    
    temp_sum=0
    for x in arr:
        if x-mid>0:
            temp_sum += (x-mid)
    
    #print(mid, temp_sum)
    
    if temp_sum<m:
        high = mid-1
    else:
        result = mid
        low = mid+1

print(result)