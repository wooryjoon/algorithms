import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations,combinations

def sol () :
    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        temp = 0
        # 거꾸로돌면서, 바로 전 가격이 max보다 작으면 max - before ++
        # else : max = before
        maxx = -1000
        for i in range(n-1,-1,-1):
            x = arr[i]
            if x <= maxx :
                temp += maxx-x
            else :
                maxx = x
        ans.append(temp)
    return '\n'.join(map(str,ans))            


print(sol())