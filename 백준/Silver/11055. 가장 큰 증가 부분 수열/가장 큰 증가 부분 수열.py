import sys
import math
input = sys.stdin.readline
A = int(input())
arr = list(map(int,input().split()))
dp = [arr[i] for i in range(A)]
# 1 100 2 50 60 3 5 6 7 8
for i in range(A) :
    for j in range(i) :
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]
print(max(dp))