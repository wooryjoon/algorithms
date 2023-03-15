import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations,combinations

def sol () :
    # sumBoard에 각각 가로합 세로합을 구해놓고, 
    n,m = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    question = [list(map(int,input().split())) for _ in range(m)]
    sumBoard = [[0]*(n+1) for _ in range(n+1)]
    sumBoard[1][1] = board[0][0]
    ansArr = []

    for i in range(1,n+1):# i = 1
        for j in range(1,n+1): # j = 1
            sumBoard[i][j] = board[i-1][j-1] + sumBoard[i-1][j]+sumBoard[i][j-1] - sumBoard[i-1][j-1]
    for e in question :
        x1,y1,x2,y2 = e
        ans = sumBoard[x2][y2] - sumBoard[x1-1][y2] - sumBoard[x2][y1-1] + sumBoard[x1-1][y1-1]
        ansArr.append(ans)
    return '\n'.join(map(str,ansArr))
print(sol())