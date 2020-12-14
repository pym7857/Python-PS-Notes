# https://suri78.tistory.com/183
# 아이디어:
# 입력받은 각 단어들이 위치한 "자릿수를" 각 알파벳마다 기록해준다.(중요도)
# 예를 들어, ABC = A*100 + B*10 + C*1이다.
# 그럼 alphabet[A] = 100, alphabet[B] = 10, alphabet[C] = 1 이 되는 것이다.

# 이런 식으로 ABC + BCA를 한다고 해보자. 그러면 alphabet리스트의 A, B, C의 값은 다음과 같을 것이다.
# alphabet[A] = 101
# alphabet[B] = 110
# alphabet[C] = 11

n = int(input())

arr = []

for _ in range(n):
    arr.append(str(input()))

alpha = [0]*26 # 알파벳은 26개 이다.

for a in arr:
    imp = 10**(len(a)-1)
    for b in a:
        alpha[ord(b)-65] += imp
        imp //= 10
#print(alpha)

# 자릿수로 가중치 매겨놨으니까, dict 쓸 필요 X
alpha = sorted(alpha, reverse=True)

ans = 0
num = 9
for c in alpha:
    ans += c * num
    num -= 1
print(ans)

