import sys
import copy
from collections import deque
input = sys.stdin.readline

# (likes,빈칸,x,y)
# 1. 스택으로 담기
# 2. 빈칸기준 내림차순 정렬
# 3. x기준 오름차순 정렬
# 4. y 기준 오름차순 정렬


N = int(input())
board = [[0] * N for _ in range(N)]
dx = (0,0,1,-1)
dy = (1,-1,0,0)
visited = [[0]*N for _ in range(N)]
dict = {}
def func1(board,likes,stack):
    for x in range(N):
        for y in range(N):
            if board[x][y] != 0 : continue
            like_cnt = 0
            empty_cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N :
                    if board[nx][ny] in likes : like_cnt += 1
                    elif board[nx][ny] == 0 : empty_cnt += 1
            arr = (like_cnt,empty_cnt,x,y)
            if not stack :
                stack.append(arr)
                continue
            else :
                if stack[-1][0] < like_cnt :
                    stack = []
                    stack.append(arr)
                elif stack[-1][0] == like_cnt: stack.append(arr)
    return stack
def func2(stack,i):
    if i == 1: stack.sort(key = lambda x : -x[i])
    else :
        stack.sort(key=lambda x: x[i])
    cnt = 0
    temp = []
    val = stack[0][i]
    for e in stack:
        if val == e[i] :
            cnt += 1
            temp.append(e)
    # 같은 값만 담기
    return temp
def extractScore(board):
    ans = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                nx,ny = i+dx[k],j+dy[k]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in dict[board[i][j]]:
                    cnt += 1
            if cnt >= 1 : ans += 10 ** (cnt-1)
    return ans
for _ in range(N**2):
    stack = []
    student,a,b,c,d = list(map(int,input().split()))
    dict[student] = [a,b,c,d]
    # 1번 연산
    stack = func1(board,[a,b,c,d],stack)

    if len(stack) == 1 :
        like,empty,x,y = stack[0]
        board[x][y] = student
        visited[x][y] = 1
        continue
    stack = func2(stack,1)
    if len(stack) == 1:
        like, empty, x, y = stack[0]
        board[x][y] = student
        visited[x][y] = 1
        continue
    stack = func2(stack,2)
    if len(stack) == 1:
        like, empty, x, y = stack[0]
        board[x][y] = student
        visited[x][y] = 1
        continue
    stack = func2(stack,3)
    like, empty, x, y = stack[0]
    board[x][y] = student
    visited[x][y] = 1
print(extractScore(board))

