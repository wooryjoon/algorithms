import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 종이의 전체값이 1과0이 섞여있으면 분할 아니면 놔둠.
    # 그 4등분한 색종이에서도 전체가 차있지 않으면 4등분
    # 재귀?
    
# 아이디어
    # 섞인지 안섞인지 판별하는 함수
    # 안섞인거면 blue white 체크해서 변수 ++
    # 섞인거면 색종이 분할해서 다시 1번함수 실행
# 변수
    # white, blue

N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
blue = 0
white = 0

def isFilled (board) :
    start = board[0][0]
    for x in board :
        for y in x :
            if y !=start : # 섞였다.
                return False
    return True
def seperate(board,N) :
    arr = []
    temp = []
    for i in range(N//2) :
        row = []
        for j in range(N//2) :
            row.append(board[i][j])
        temp.append(row)
    arr.append(temp)
    
    temp = []
    for i in range(N//2) :
        row = []
        for j in range(N//2,N):
            row.append(board[i][j])
        temp.append(row)
    arr.append(temp)

    temp = []
    for i in range(N//2,N) :
        row = []
        for j in range(N//2):
            row.append(board[i][j])
        temp.append(row)
    arr.append(temp)

    temp = []
    for i in range(N//2,N) :
        row = []
        for j in range(N//2,N):
            row.append(board[i][j])
        temp.append(row)
    arr.append(temp)

    return arr

def recur (board) :
    global blue,white
    if isFilled(board) :                   #안섞여있으면
        if board[0][0] == 1:
            blue += 1
        elif board[0][0] == 0 :
            white += 1
    else :                                 # board가 섞여있으면
        arr = seperate(board,len(board))
        for x in arr :
            recur(x)

recur(board)
print(white)
print(blue)