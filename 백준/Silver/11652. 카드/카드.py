import sys
from collections import deque, defaultdict
input = sys.stdin.readline
from heapq import heappop,heappush,heapify
# 문제 정리

# 아이디어
    # 1. 길이가 짧은게 우선, 
    # 2. 자리수의 합을 비교해서 작은게 우선
    # 3. 만약 1,2로 비교 안되면 사전순으로 비교한다
# 시간복잡도

# 변수계획

n = int(input())
arr = [int(input()) for _ in range(n)]
dict = {}

for x in arr:
    if not  dict.get(x):
        dict[x] = 1
    elif dict[x]:
        dict[x] += 1
temp = []
for x in dict.keys():
    temp.append([dict[x],x]) # 횟수,숫자
temp.sort(key = lambda x :(-x[0],x[1]))
print(temp[0][1])