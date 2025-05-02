import sys
from collections import deque
input = sys.stdin.readline

T = []
for _ in range(4):
    T.append(deque(map(int, input().rstrip())))

K = int(input())

for _ in range(K):
    match = [T[0][2] == T[1][6], T[1][2] == T[2][6], T[2][2] == T[3][6]]
    n, d = map(int, input().split())
    
    T[n-1].rotate(d)
    li = []
    for i in range(4):
        if i == n-1:
            continue
        li.append(i)
    print("li:", li)
    
    if n <= 2:
        for i, m in enumerate(match):
            print(match)
            T[li[i]].rotate(m)

    else:
        for i, m in enumerate(match[::-1]):
            print(match)
            T[li[2-i]].rotate(m)

res = 0
for i, t in enumerate(T):
    res += t[0] * (2**i)
    print("xx", res)
print(res)