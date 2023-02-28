import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # dp
# 아이디어
    # d[1] = 1
    # d[2] = 2          00 11
    # d[3] = 3          001 100 111
    # d[4] = 5          0011 11001 1111 (d3)    
    # d[5] = 
#시간복잡도

n = int(input())
d = [0] * 1000010

d[1] = 1
d[2] = 2
d[3] = 3

for i in range(4,n+1) :
    d[i] = d[i-1]%15746 + d[i-2]%15746
print(d[n]%15746)
