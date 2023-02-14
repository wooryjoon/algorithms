import sys
input = sys.stdin.readline
from bisect import bisect_left ,bisect_right
from collections import deque

# 문제정리
    # 길이가 4인 테트로미노 (5가지)를 board에 적절히놓아서
    # 놓인 칸에 써있는 값의 합이 최대가 되도록 하게.
    # 결국 depth가 4 인 DFS 탐색 아닌가?
    # ㅓㅏ ㅗ ㅜ 를 제외한 모든 꼴은 DFS로 해결 가능.
    # ㅓㅏㅗㅜ는 DFS 함수 내에서 새롭게 가능
# 아이디어

# 시간복잡도

N,M = map(int,input().split()) # 행 열
board = [list(map(int,input().split())) for _ in range(N)] # board
visited = [[0]*M for _ in range(N)]
maxValue = max(map(max,board))
ans = -1000
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def DFS (x,y,depth,sums) :
    global ans
    # 종료조건
    if sums + maxValue*(4-depth) <= ans:
        return
    if depth == 4 :
        ans = max(ans,sums)
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0 :
            if depth == 2 :
                visited[nx][ny] = 1
                DFS(x,y,depth+1,sums+board[nx][ny])
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            DFS(nx,ny,depth+1,sums+board[nx][ny])
            visited[nx][ny] = 0

for i in range(N) :
    for j in range(M) :
        visited[i][j] = 1
        DFS(i,j,1,board[i][j])
        visited[i][j] = 0
print(ans)
