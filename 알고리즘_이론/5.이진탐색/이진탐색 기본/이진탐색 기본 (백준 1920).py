# 제시된 리스트
n = int(input())
lst = input().split()
lst = list(map(int, lst))

# 찾고자 하는 값있는 리스트
m = int(input())
lst2 = input().split()
lst2 = list(map(int, lst2))

lst = sorted(lst) # 이진 탐색 = 정렬이 가장 우선

def binarySearch(low, high, a):
    if low > high:
        return 0
        
    middle = (low+high)//2
        
    if lst[middle] == a:
        return 1
    elif lst[middle] > a:
        return binarySearch(low, middle-1, a)
    elif lst[middle] < a:
        return binarySearch(middle+1, high, a)
    

for a in lst2: # a = 찾고자 하는 값
    low = 0
    high = len(lst)-1
    print(binarySearch(low, high, a))
    
        
