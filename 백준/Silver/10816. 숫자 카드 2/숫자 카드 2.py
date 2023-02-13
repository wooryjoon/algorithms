import sys
input = sys.stdin.readline
from bisect import bisect_left ,bisect_right

# 문제정리

# 아이디어

# 시간복잡도

M = int(input())
total = list(map(int,input().split()))
N = int(input())
arr = list(map(int,input().split()))
total.sort()

for target in arr :
    # target을 찾기 위해 이분 탐색
    a,b = 0,0
    a = bisect_left(total,target)
    b = bisect_right(total,target)
    print(abs(a-b))
