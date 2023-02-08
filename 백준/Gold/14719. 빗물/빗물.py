import sys
import copy
from collections import deque, defaultdict
from itertools import combinations
input = sys.stdin.readline
# 문제 정리
    # 반복하면서
    # 1이 한번 등장하면 그때부터  0카운트 시작
    # 그 이후 1이 나오면 0카운트 햇던거 ans에 더해줌
    # 근데 1이 안나오고 
# 아이디어

# 시간복잡도

# 변수 
H,W = list(map(int,input().split())) # 세로,가로
blocks = list(map(int,input().split()))
board = [[0 for _ in range(W)] for _ in range(H)]

for i in range(W):
    for j in range(H-1,H-blocks[i]-1,-1):
        board[j][i] = 1

count = 0            
for arr in board :
    oneFlag = False
    water = 0
    for i in range(len(arr)):
        x = arr[i]
        if x == 1 :
            if oneFlag == False :
                oneFlag = True
            if oneFlag == True :
                count += water
                water = 0
            continue
        if x == 0 :
            if oneFlag == True :
                water += 1
            continue
print(count)