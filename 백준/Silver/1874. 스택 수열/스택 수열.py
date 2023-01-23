import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sortedArr = deque([i for i in range(1,n+1)])
inputArr = []
generater = []
stack = []
cur = 1
flag = False
for _ in range(n):
    x = int(input()) # value 4,3,6,8,7,5,2,1
    # push 결정
    while (cur <= x):
        cur += 1
        stack.append(sortedArr.popleft())
        generater.append('+')
    # pop 결정
    if stack[-1] != x : # 스택의 top이 x가 아니라면
        flag = True
        break
    else :
        stack.pop()
        generater.append('-')

if flag : 
    print('NO')
else : print('\n'.join(generater))
    
        
        