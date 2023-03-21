import sys

input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 스택에 푸쉬하는 순서는 무조건 오름차순 순서대로 간다.   
# 아이디어

# 변수 사용 계획

# 시간 복잡도

n = int(input())
ans = []
arr = [int(input()) for _ in range(n)]
currNum = 1 # push할때 들어갈 수
currTop = 0
stack = deque()
stack.append(0)
flag = True
for currInput in arr :
    while currNum <= currInput:
        stack.append(currNum)
        ans.append('+')
        currNum += 1;
    if stack[-1] > currInput : 
        print('NO')
        flag = False
        break
    else : 
        stack.pop()
        ans.append('-')
    

if flag :
    print('\n'.join(ans))
