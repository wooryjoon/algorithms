import sys
input = sys.stdin.readline
from collections import deque
n,m = list(map(int,input().split()))# 랜선 개수, 필요한 랜선 갯수
arr = [int(input()) for _ in range(n)]

    # 랜선의 길이를 1부터 완탐해도되지만 이탐하자.
    # left,right를 정하고, mid로잘랐을때 m개보다 개수가 작개나오면
    # right = mid -1
    # 반대면 left = mid + 1인데, 최대를 구해야하므로 m개가나와도 left = mid +1

left = 1
right = max(arr)
mid = (left+right) // 2
while (left <= right) :
    mid = (left+right) // 2
    count = 0
    for x in arr :
        count += x // mid
    if count < m :
        right = mid -1 # 더 짧게 잘라야한다.
    else :
        left = mid + 1
print(right)