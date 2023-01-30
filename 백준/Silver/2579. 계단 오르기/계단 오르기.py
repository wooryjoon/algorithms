import sys
import copy
from collections import deque
input = sys.stdin.readline

#[문제 정리]
# 각 계단에 도달할때의 최대값을 dp테이블에 저장하여서 풀기.
# [아이디어]
# d[1] = t[1]
# d[2] = d[1] + t[2]
# d[3] = d[1] + t[3]
# d[4] = 1,3 or 2 + t[4] = d[3] or d[2] + t[4]
# d[n] = d[n-1] + t[n] or d[n-2] + t[n]
# [시간복잡도]

# [변수 사용계획]

T = int(input()) # 층수
s = [0]

for _ in range(T):
    s.append(int(input()))

def solution (T) :
    if T == 1 : return s[1]
    if T == 2: return s[1] + s[2]
    if T == 3: return max(s[1]+s[3],s[3]+s[2])
    d = [0] * (T+1)
    d[1] = s[1]
    d[2] = s[1] + s[2]
    d[3] = max(s[1]+s[3],s[3]+s[2])
    for i in range(4,T+1):
        d[i] = max(d[i-2] + s[i],d[i-3] + s[i-1] + s[i])
    return d[T]
print(solution(T))
