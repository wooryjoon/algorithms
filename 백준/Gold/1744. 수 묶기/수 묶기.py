import sys

input = sys.stdin.readline
from collections import deque

# 합이 최대가 되려면?
    # 음수는 음수끼리 묶기, 음수가 1개 남으면 안묶기
    # N N은 50보다 작다.
    # 
    # -3 -2 -1 0 5
    # -3 -2 -1 0 2 3
n = int(input())
arr = [int(input()) for _ in range(n)]
minusArr = []
plusArr = []

for e in arr :
    if e <= 0 :minusArr.append(e)
    else :plusArr.append(e)
plusArr.sort()
minusArr.sort(reverse=True)

plusI = len(plusArr)-1
minusI = len(minusArr)-1

def extractAns(i,arr):
    ans = 0
    while i >= 0 :
        if i == 0 : 
            ans += arr[i]
            break
        if arr[i] * arr[i-1] >= arr[i] + arr[i-1]:
            ans += arr[i] * arr[i-1]
            i = i - 2
        elif arr[i] * arr[i-1] < arr[i] + arr[i-1]:
            ans += arr[i]
            i = i - 1    
    return ans
ans1 = extractAns(plusI,plusArr)
ans2 = extractAns(minusI,minusArr)

print(ans1+ans2)
