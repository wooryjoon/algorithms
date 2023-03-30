import sys
import math
import copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations
# 123
# 213
# 231
# 321
# 만약 N이 한자리수라면 교환 불가.
# N = 12345, M = 5
#1 <= i < j <= 5 -> (1,2) (1,3) (1,4) (1,5)...
# 위치바꾼 수의 앞자리가 0으로 시작하면 안된다?
# i,j의 쌍을 DFS로 모두 구하고, 앞자리가 0이 되지 않는 수 중 최대값 구하기

N,K = list(map(int,input().split()))
length = 0
value = N
ways = []
ans = -1
while N != 0:
    N = N // 10
    length += 1
ways = list(combinations([i for i in range(1,length+1)],2))

def change (num,i,j):
    i = i-1
    j = j-1
    arr = list(str(num))
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    if arr[0] == '0' : return False
    else : return int(''.join(arr))

def BFS() :
    global ans
    q = set()
    q.add((value,0)) # 현재 값, 남은 횟수
    flag = False
    while q :
        curr,cnt = q.pop()
        if cnt == K : # K번 연산 했으면
            flag = True
            ans = max(ans,curr) # k번 연산했을때의 값과 기존 최대값 비교갱신
            continue
        for e in ways :
            i,j = e
            next = change(curr,i,j)
            if next == False : continue # 앞자리가 0인 경우
            q.add((next,cnt+1))
    if not flag : return False
    return True
if BFS(): # K번 연산 수행 했으면?
    print(ans)
else : print(-1)
