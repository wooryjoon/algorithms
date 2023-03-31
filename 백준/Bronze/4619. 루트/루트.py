import sys
import math
import copy
input = sys.stdin.readline
from collections import deque 
from itertools import combinations
import heapq
# 숫자를 1부터 ~ B까지 돌린다
# 반복문 내에서 N승을 해주면서 차이값과 A를 튜플로 묶어 배열에 저장
# 최종 배열을 오름차순 정렬 후에 0번째 항의 A를 출력

arr = []
ans = []
while True :
    B,N = list(map(int,input().split()))
    if not B and not N : break
    i = 1
    while i ** N < B:
        diff = abs(i ** N - B)
        heapq.heappush(arr,(diff,i))
        i += 1
    diff = abs(i ** N - B)
    heapq.heappush(arr,(diff,i))
    ans.append(arr[0][1])
    arr = []
print('\n'.join(map(str,ans)))
