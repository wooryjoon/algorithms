import sys
import math
import copy
input = sys.stdin.readline
from collections import deque 
from itertools import combinations
import heapq

# 메시지  : 숫자N개로 이루어진 수열
# 각 숫자는 모두 C보다 작거나 같다.
# 숫자를 빈도순으로 정렬.
# 각 값이 몇번 나오는지 map으로 파악. *
# 빈도수가 같으면 먼저 나온 값을 먼저 출력. **

# arr을 돌면서 (빈도수,등장 순서)
N,C = list(map(int,input().split()))
arr = list(map(int,input().split()))
hashMap = {}
temp = []
ans = []
for i in range(N):
    e = arr[i]
    if e in hashMap:
        hashMap[e][0] += 1
    else :
        hashMap[e] = [1,i]
temp = [[i,j] for i,j in hashMap.items()]
temp.sort(key=lambda x:(-x[1][0],x[1][1])) # 빈도수, 우선순위 정렬
for i,j in temp :
    ans += [i] * j[0]
print(*ans)

