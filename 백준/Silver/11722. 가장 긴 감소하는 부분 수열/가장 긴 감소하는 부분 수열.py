import sys
import math
input = sys.stdin.readline
A = int(input())
arr = list(map(int,input().split()))
dp = [1] * A

# 1 100 2 50 60 3 5 6 7 8
for i in range(A):
    for j in range(i):
        if arr[i] < arr[j]: # 수열 길이 증가 가능.
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))