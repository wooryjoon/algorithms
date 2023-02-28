import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # d[1] = 1
    # d[2] = 2
    # d[3] = 1+2, 2+1, 1+1+1, 3 == 4
    
# 아이디어

#시간복잡도
n = int(input())
arr = [int(input()) for _ in range(n)]
d = [0] * 20

def solution (n,d) :
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4,20) :
        d[i] = d[i-3]+d[i-2]+d[i-1]
    for x in arr :
        print(d[x])
solution(n,d)