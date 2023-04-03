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
    if hashMap.get(e):
        hashMap[e][0] += 1
    else :
        hashMap[e] = [1,i]
for key in hashMap :
    freq,order = hashMap[key]
    temp.append([freq,order,key])
temp.sort(key=lambda x:(-x[0],x[1]))

for e in temp :
    freq,order,key = e
    for i in range(freq):
        ans.append(key)
print(' '.join(map(str,ans)))

