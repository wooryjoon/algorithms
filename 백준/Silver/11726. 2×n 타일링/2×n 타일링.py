import sys
import copy
from collections import deque
input = sys.stdin.readline
#아이디어
# dp문제 (메모이제이션)
# n이 홀수 : d[n-1] + 1
# n이 짝수 : d[n-2] + 2
# 시간복잡도
# 선형탐색
# 변수 사용 계획
# 
n = int(input()) # 계단 갯수

def solution (n) :
    d = [0] * (n+1)
    if n == 1 : return 1
    if n == 2 : return 2
    d[1] = 1
    d[2] = 2

    for i in range(3,n+1):
        d[i] = d[i-2] % 10007 + d[i-1] % 10007
    return d[n]
print(solution(n) % 10007)