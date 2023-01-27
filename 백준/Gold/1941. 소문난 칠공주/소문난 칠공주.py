import sys
from collections import deque
input = sys.stdin.readline

#[문제 정리]
# 5X5 테이블
# 7명, 가로/세로로 인접, 7명중 S가 4명 이상.
# [아이디어]
# 배열을 1차원으로 펴놓고 !!!! 
# 그중에 7개를 고른다. (DFS) ( 1차원으로 편 배열 이용) (좌표값을 배열에담아 넘기기)
# 고르다가 Y가 4개 이상이면 거기서 스탑, 
#  정제된 고른 배열로 BFS를 돌린다. (2차원배열 맵 이용해서 받아온 좌표값들이 연결된지 확인)
# BFS에서 연결되어있음이 확인되면 카운트 + 1

# [시간복잡도]

# [변수 사용계획]
# dx dy visited1(1차원), visited2(2차원)

board = [list(input().rstrip()) for _ in range(5)]
board2 = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
cnt = 0

for i in range(5):
    for j in range(5):
        board2.append(board[i][j])
def BFS (arr) :
    count = 0
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for x in arr:
        visited[x[0]][x[1]] = 1
    queue = deque()
    queue.append(arr[0])
    while (queue):
        [x,y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and visited[nx][ny] == 1 :
                count += 1
                queue.append([nx,ny])
                visited[nx][ny] = 0
    if count == 7 : return True
    else : return False

def DFS(arr,depth,startIndex,Ycount) : # 25개중에 조합으로 7개 뽑기
    global cnt
    if Ycount >= 4:
        return
    if depth == 7:
        # 붙은건지 확인
        if BFS(arr) == True :
            cnt += 1
            return
    for i in range(startIndex,25):
        arr.append([i//5,i%5])
        if board2[i] == 'Y' : Ycount += 1
        DFS(arr,depth+1,i+1,Ycount)
        if board2[i] == 'Y' : Ycount -=1
        arr.pop()
DFS([],0,0,0)
print(cnt)