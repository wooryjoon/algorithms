import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

# 아이디어
    # 만약 카운트가 남아있다면


def sol () :
    n,chance = list(map(int,input().split()))
    arr =  list(map(int,input().split()))
    k = 0
    currLength = 0
    maxx = -1000
    p1 = 0
    p2 = 0
    # 최초의 p1, p2 설정 완료
    while p1 < n and p2 < n and p1 <= p2 :
        if arr[p2] % 2 == 0 :
            currLength += 1
            p2 += 1
        elif arr[p2] % 2 == 1 :
            if k >= chance : # 찬스를 다 쓴 상태라면
                if arr[p1] % 2 == 1 :
                    k -= 1
                elif arr[p1] % 2 == 0 :
                    currLength -= 1
                p1 += 1
            else : # 찬스를 다 안쓴 상태라면
                k += 1
                p2 += 1
        maxx = max(maxx,currLength)
    return maxx

print(sol())