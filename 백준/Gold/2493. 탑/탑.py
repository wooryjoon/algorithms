import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 탑의 갯수
ans = ['0']
stack = []
towerHeights = list(map(int,input().split()))

# 스택에 왼쪽부터 값을 넣고
# 다음에 들어올 수가 스택의 top보다 크다면 stack을 pop하고 다음 수를 push
# 다음에 들어올 수가 스택의 top보다 작다면 (수신가능) ans에 해당 인덱스 삽입
stack.append([towerHeights[0],1])
for i in range(1,n):
    x = towerHeights[i]
    while stack:
        if stack[-1][0] < x :
            stack.pop()
        else : break
    if len(stack) == 0 : ans.append('0')
    else :
        ans.append(str(stack[-1][1]))
    stack.append([x,i+1])
print(' '.join(ans))