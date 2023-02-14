import sys
input = sys.stdin.readline
from bisect import bisect_left ,bisect_right
from collections import deque

# 문제정리
    # 배열에서 두 수를 골라서 차이를 계산
    # 그 차이가 M이상이면 pick하고, 그 차이값을 저장
    # minValue로 차이값의 최소를 계속해서 갱시
    # 완전탐색? -> 시간초과, 투포인터.
# 아이디어
    # 배열을 오름차순 정렬
    # 차이가 M이상이면 left ++, 차이 기록
    # 차이가 M미만이면 right ++
# 시간복잡도
    # O(2N)

n,m = list(map(int,input().split()))
arr =[]
for _ in range(n) :
    arr.append(int(input()))
arr.sort()
minValue = sys.maxsize
left = 0
right = 0
while left != n :
    if right == n :break
    value = arr[right] - arr[left]
    if value >= m :
        minValue = min(minValue,value)
        left += 1
    elif value < m :
        right += 1
        
print(minValue)