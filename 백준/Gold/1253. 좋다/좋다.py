import sys
import copy
input = sys.stdin.readline
from collections import deque

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0
visited = [0] * 2100

for i in range(n):
    currNum = arr[i]
    visited[i] = 1
    left = 0
    right = n-1
    while left < right :
        if visited[left] == 1 :
            left +=1
            continue
        if visited[right] == 1 :
            right -= 1
            continue

        _sum = arr[left]+arr[right]
        if _sum > currNum:
            right -= 1
        elif _sum == currNum:
            cnt += 1
            break
        elif _sum < currNum:
            left += 1
    visited[i] = 0
print(cnt)


