import sys
import math
import copy
input = sys.stdin.readline
from collections import deque
from itertools import combinations


# 행 체크, 열 체크, 박스 체크
board = [list(map(int,input().split())) for _ in range(9)] # 9*9 board 완성

# 백트래킹, 만약 board[i][j]가 0 이라면, 수를 하나 넣어야하는 것.
# 어떤 수를 넣을지? -> 열 체크, 행 체크, 박스 체크
check1 = [[0]*9 for _ in range(9)] # 행 체크
check2 = [[0]*9 for _ in range(9)] # 열 체크
check3 = [[0]*9 for _ in range(9)] # 작은 박스는 총 9개가 나오므로.
def box(x,y) :
    #(x,y) 좌표가 몇번 박스에 속해있는가?
    # x가 0~2라면 0번행 3~5라면 1번행 6~8 2번행
    # y가 0~2라면 0번열 3~5라면 1번열 6~8 2번열
    # 그렇다면 속해있는 박스의 번호는?
    # x // 3 * 3 + y // 3
    return (x // 3) * 3 + (y // 3)
for i in range(9):
    for j in range(9):
        if board[i][j] : # board에 숫자가 채워져있음.
            num = board[i][j]-1
            check1[i][num] = 1 # i번째 행에 num이라는 숫자가 있다.
            check2[j][num] = 1 # j번째 열에 num이라는 숫자가 있다.
            check3[box(i,j)][num] = 1 # 해당 박스에 num이라는 숫자가 있다.

def DFS(x,y) :
    #종료조건
    if x == 9:
        # 해당 board 전체 출력
        for e in board:
            print(*e)
        exit(0)
    # 만약 현재 살펴보고 있는 칸이 숫자로 차있으면 다음칸
    if board[x][y] :
        DFS(x+(y+1)//9,(y+1)%9)
        return
    # 만약 현재 살펴보고 있는 칸에 어떤 수를 넣어야 한다?
    # 1~9중 어떤 것을 넣을 수 있을까?
    for i in range(9):
        # 행,열, 작은 박스 중 하나라도 걸리는 숫자는 Skip
        if check1[x][i] or check2[y][i] or check3[box(x,y)][i]: continue
        board[x][y] = i+1 # 보드에 들어가는건 0~8이 아닌 1~9
        check1[x][i] = 1
        check2[y][i] = 1
        check3[box(x,y)][i] = 1
        DFS(x+(y+1)//9,(y+1)%9)
        board[x][y] = 0 # 보드에 들어가는건 0~8이 아닌 1~9
        check1[x][i] = 0
        check2[y][i] = 0
        check3[box(x,y)][i] = 0

DFS(0,0)



