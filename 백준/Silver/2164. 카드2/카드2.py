import sys
from collections import deque, defaultdict
input = sys.stdin.readline
from heapq import heappop,heappush,heapify
# 문제 정리

# 아이디어

# 시간복잡도

# 변수계획

n = int(input())
arr = [i for i in range(1,n+1)]
arr = deque(arr)
while len(arr) != 1:
    arr.popleft()
    arr.append(arr.popleft())

print(arr[0])