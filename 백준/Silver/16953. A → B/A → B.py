import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
# 곱하기 2, 자리수 1 추가 2가지 경우
A,B = list(map(int,input().split()))
def BFS():
    q = deque()
    q.append([A,0])
    visited = set()
    visited.add(A)
    while q :
        num,count = q.popleft()
        if num > 10**9 : continue
        if num == B :
            return count + 1
        for i in range(2):
            nextNum = 0
            if i == 1 :nextNum = num * 2
            if i == 0 :nextNum = int(str(num)+'1')
            if nextNum in visited : continue
            visited.add(nextNum)
            q.append([nextNum,count+1])
    return -1

print(BFS())