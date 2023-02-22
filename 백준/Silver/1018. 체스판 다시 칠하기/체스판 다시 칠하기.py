import sys
input = sys.stdin.readline
from collections import deque
import copy
# 아이디어
    # 좌표를 돌면서 8*8 case 가짓수 구하기
    # 결국 둘중하나다. 0,0이 w이거나 b이거나.
    # 위 두 케이스를 모두 해보고 최소값 찾기
    # 0,0에서 출발하는 BFS. inputsize가 작으므로 가능할듯?

N,M = list(map(int,input().split()))
board = [list(input().strip()) for _ in range(N)]
ans = float('inf')
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def makeMap (x,y) :
    newMap = [[0]*(8) for _ in range(8)]
    for i in range(0,8):
        for j in range(0,8):
            newMap[i][j] = board[i+x][j+y]
    return newMap

def BFS (maps,startColor) :
    # maps의 0,0이 B인 경우에 바꿔야
    visited = [[0]*8 for _ in range(8)]
    count = 0
    queue = deque()
    visited[0][0] = 1
    if maps[0][0] != startColor: count += 1;
    maps[0][0] = startColor;
    queue.append((0,0))

    while queue :
        x,y= queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<8 and 0<=ny<8 and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if maps[x][y] == maps[nx][ny] :
                    count += 1
                    if maps[x][y] == 'B' : maps[nx][ny] = 'W'
                    elif maps[x][y] == 'W' : maps[nx][ny] = 'B'
                queue.append((nx,ny))
    return count



for i in range(N) :
    for j in range(M) :
        if i >= N-8+1: continue
        if j >= M-8+1 : continue
        newMap = makeMap(i,j) # 나올수있는 체스판의 case
        map1 = copy.deepcopy(newMap) # 두가지 케이스 실험
        ans = min(ans,BFS(map1,'B'))
        map2 = copy.deepcopy(newMap)
        ans = min(ans,BFS(map2,'W'))
print(ans)