import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # LIS 알고리즘
# 아이디어

#시간복잡도

n = int(input())

d = [1] * n
arr = list(map(int,input().split()))

#d[i] = i번쨰 항까지 LIS의 최대값

for i in range(1,n):
    for j in range(0,i):
        if arr[i] > arr[j] :
            d[i] = max(d[i],d[j]+1)
print(max(d))






