import sys
input = sys.stdin.readline
from collections import deque

# N개의 자연수 집합 U
# 적당히 세 수를 골라서 합을 구했을 때, 그 합이 U에 포함되는 경우중에 가장 큰 D


# 오름차순 정령
# 세 수 정하기. (반복문 + 투 포인터) 2N^2
# 각 분기마다 d가 U에 포함되는가 check.(dict로 해볼까)
# 결국 구하고자 하는 것은 K번째 수다.
# 

n = int(input())
arr = [int(input()) for _ in range(n)]
ans = []
sums  = {}
# 이항을 통해 해결.
# a+b = d-c

for i in range(n):
    for j in range(n):
        sums[arr[i]+arr[j]] = 1

for i in range(n):
    for j in range(n):
        if sums.get(arr[i]-arr[j]) : # 조건을 만족하는 a,b,c,d,가 있다
            ans.append(arr[i]) # 해당하는 d 값을 ans에 추가.

ans.sort()
print(ans[-1])