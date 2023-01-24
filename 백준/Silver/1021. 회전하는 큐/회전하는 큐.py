import sys
from collections import deque
input = sys.stdin.readline

n,m = list(map(int,input().split())) # n : 큐크기 m : 뽑아내려는 갯수
# 뽑고자 하는게 중간보다 작으면 popleft해서 뒤로붙임
# 뽑고자 하는게 중간보다 크면 pop해서 앞으로 붙임

locations = list(map(int,input().split()))
arrays = deque([i for i in range(1,n+1)])

cnt = 0
for x in locations :
    length = len(arrays) 
    temp = arrays.index(x)
    if temp < length - temp :
        while(True):
            if arrays[0] == x:
                arrays.popleft()
                break
            else :
                arrays.append(arrays.popleft())
                cnt += 1
    else :
        while(True):
            if arrays[0] == x:
                arrays.popleft()
                break
            else :
                arrays.appendleft(arrays.pop())
                cnt += 1
print(cnt)