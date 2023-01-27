import sys
import copy
from collections import deque
input = sys.stdin.readline

#[문제 정리]
# 1~5 : cctv번호 6 : 벽
# 벽은 통과 불가능
# CCTV는 통과 가능
#CCTV의 비추는 각도의 Case를 DFS완전탐색을 통해 구한다.
# 그 중에 사각지대의 최소 크기를 출력한다.
# depth가 CCTV의 개수와 동일해질때가 종료조건
# [아이디어]
# 각 CCTV마다 함수를 따로 구현해서, 2차원배열에서 연산하는 함수를 만들고
# 각 CCTV마다 4방향으로 돌린다.
# 서로다른위치인데 DFS로 어떻게 연결 ? : 먼저좌표를따고
# [시간복잡도]

# [변수 사용계획]
# 갱신해줄 min

# 순서 : 동 남 서 북
n,m = list(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
cctvLength = 0
cctvLocation = []
mins = 1000
for i in range(n) : # cctv개수 구하기
    for j in range(m) :
        if 1<=board[i][j]<=5:
            cctvLength += 1
            cctvLocation.append([i,j])
cctvLocation.append('Dummy')
def CCTV1 (newMap,x,y,i) :
    if i == 0: 
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
    if i == 1 :
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
    if i == 2 : 
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
    if i == 3 : 
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
def CCTV2 (newMap,x,y,i) :
    if i == 0 : # 동서
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
    if i == 1 : #남북
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
def CCTV3 (newMap,x,y,i) :
    if i == 0:
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
    if i == 1:
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
    if i == 2:
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
    if i == 3:
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
def CCTV4 (newMap,x,y,i) : 
    if i == 0:
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
    if i == 1:
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
    if i == 2:
        # 동
        for j in range(y,m):
            if newMap[x][j] == 6:
                break
            if newMap[x][j]== 0 :
                newMap[x][j] = '#'
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
    if i == 3:
        # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
        # 서
        for j in range(y,-1,-1):
            if newMap[x][j] == 6:
                break
            if newMap[x][j] == 0 :
                newMap[x][j] = '#'
        #북
        for j in range(x,-1,-1):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'
def CCTV5 (newMap,x,y) : 
    #북
    for j in range(x,-1,-1):
        if newMap[j][y] == 6 :
            break
        if newMap[j][y] == 0 :
            newMap[j][y] = '#'
    # 동
    for j in range(y,m):
        if newMap[x][j] == 6:
            break
        if newMap[x][j]== 0 :
            newMap[x][j] = '#'
    # 서
    for j in range(y,-1,-1):
        if newMap[x][j] == 6:
            break
        if newMap[x][j] == 0 :
            newMap[x][j] = '#'
    # 남
        for j in range(x,n):
            if newMap[j][y] == 6 :
                break
            if newMap[j][y] == 0 :
                newMap[j][y] = '#'

def DFS (currLocation,depth,maps) : 
    global mins
    if depth == cctvLength :
        count = 0
        for x in maps:
            for y in x :
                if y == 0 :
                    count += 1
        mins = min(mins,count)
        return
    [x,y] = currLocation
    if board[x][y] == 1: # 4번
        for i in range(4):
            newMap = copy.deepcopy(maps)
            CCTV1(newMap,x,y,i)
            DFS(cctvLocation[depth+1],depth+1,newMap)
    elif board[x][y] == 2: # 2번
        for i in range(2):
            newMap = copy.deepcopy(maps)
            CCTV2(newMap,x,y,i)
            DFS(cctvLocation[depth+1],depth+1,newMap)
    elif board[x][y] == 3:
        for i in range(4):
            newMap = copy.deepcopy(maps)
            CCTV3(newMap,x,y,i)
            DFS(cctvLocation[depth+1],depth+1,newMap)
    elif board[x][y] == 4:
        for i in range(4):
            newMap = copy.deepcopy(maps)
            CCTV4(newMap,x,y,i)
            DFS(cctvLocation[depth+1],depth+1,newMap)
    elif board[x][y] == 5:
        newMap = copy.deepcopy(maps)
        CCTV5(newMap,x,y)
        DFS(cctvLocation[depth+1],depth+1,newMap)

DFS(cctvLocation[0],0,board)
print(mins)