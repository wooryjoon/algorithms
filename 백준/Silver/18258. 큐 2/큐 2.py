import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 탑의 갯수
queue = deque()
for _ in range(n):
    x = input().split()
    if len(x) == 2: #push연산
        queue.append(int(x[1]))
    elif x[0] == 'pop':
        if queue:
            print(queue.popleft())
        else : print(-1)
    elif x[0] == 'size':
        print(len(queue))
    elif x[0] =='empty' :
        if queue: print(0)
        else : print(1)
    elif x[0] == 'front' :
        if queue:
            print(queue[0])
        else :print(-1)
    elif x[0] == 'back':
        if queue:
            print(queue[-1])
        else: print(-1)

