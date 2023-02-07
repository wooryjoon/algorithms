import sys
from collections import deque, defaultdict
input = sys.stdin.readline
from heapq import heappop,heappush,heapify
# 문제 정리

# 아이디어
    # 1. 길이가 짧은게 우선, 
    # 2. 자리수의 합을 비교해서 작은게 우선
    # 3. 만약 1,2로 비교 안되면 사전순으로 비교한다
# 시간복잡도

# 변수계획



n = int(input())
temp = []
for i in range(n):
    temp.append(list(input().rstrip()))

for x in temp:
    stack = deque()
    for e in x :
        if not stack :
            stack.append(e)
            continue
        if stack[-1] == '(':
            if e == ')':
                stack.pop()
                continue
            if e == '(':
                stack.append(e)
    if stack :
        print('NO')
    else : print('YES')