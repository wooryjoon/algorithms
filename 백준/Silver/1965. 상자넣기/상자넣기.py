import sys
input = sys.stdin.readline
from collections import deque

# LIS ?

# dp테이블 마련. dp[i] = 최장 수열의 길이
n = int(input())
arr = list(map(int,input().split()))
dp = [1] *(n+1) # i번째항까지 왔을때 최장 수열의 길이
for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j] :
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))