import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 동전 구성이 같은데 순서만 다른건 중복이다.
# 아이디어
    # 1원 : 1 1가지
    # 2원 : 1+1 2    2가지
    # 3원 : 111 12   2가지
    # 4원 : 1111 13 22 3가지
    # 5원 :11111 14 23 5   4가지
    # 6원 : d[k]
#시간복잡도

n,k = list(map(int,input().split())) # 동전 종류, 목표금액
coins = [int(input().strip()) for _ in range(n)]

d = [0] *(k+1)
d[0] = 1
#d[i] = i원을 만드는 경우의 수
for x in coins :
    for j in range(1,k+1):
        if j >= x :
            d[j] += d[j-x]

print(d[k])


