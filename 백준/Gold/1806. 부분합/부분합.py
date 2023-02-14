import sys
input = sys.stdin.readline
from bisect import bisect_left ,bisect_right
from collections import deque

# 문제정리
    # 연속합 구하는데, 그중에서 가장 짧은것.
    
# 아이디어
    # 연속합 투포인터로 구한다. (같은지점에서 출발)
    # 조건에 맞을 떄 길이 저장. minValue로 갱신
# 시간복잡도
    
N,S = list(map(int,input().split())) # 배열길이, S이상 값 추출
arr = list(map(int,input().split()))
left = 0
right = 0
minValue = 999999
flag = False
sums = arr[0]
while left != N:
    if sums < S :
        right += 1
        if right == N :
            break
        sums += arr[right]
        continue
    elif sums >= S :
        minValue = min(right - left + 1,minValue)
        sums = sums - arr[left]
        left += 1
        flag = True

if flag == True :
    print(minValue)
else :
    print(0)