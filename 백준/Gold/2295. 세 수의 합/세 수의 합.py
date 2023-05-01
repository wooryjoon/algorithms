import sys
from heapq import heappush
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = -10
twoSum = []
for a in range(N):
    for b in range(N):
        twoSum.append(arr[a]+arr[b])
twoSum = set(twoSum)
for d in range(N):
    for c in range(N):
        num = arr[d]-arr[c]
        if num in twoSum : # Set에서는 특정 원소 포함 여부를 상수시간에 가능
            ans = max(ans,arr[d])
print(ans)


