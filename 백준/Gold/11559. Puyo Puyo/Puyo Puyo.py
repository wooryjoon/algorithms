import sys
import copy
from collections import deque
input = sys.stdin.readline
# 문제 정리
    # 현재 Board에서 모든 점에 각각의 visited로 BFS 돌리기,
    # BFS돌리면서 칸 찍을때마다 num+1 해주면서 num이 4이상이면
    # 찍은 좌표들을 stamp배열에 저장, BFS탐색에서 건너뜀.
    # 모든 점에서 다 진행한 이후, stamp배열에서 찍어놓은 좌표들을 터트린다.
    # 한 뭉탱이라도 뿌요시켰으면 ans를 1 증가시킨다. 아니면 그대로 Break
    # Board를 새로운 Board로 교체한다.
# 아이디어
    # BFS 함수 필요.
    # stamp배열 매 연쇄마다 갱신 필요
    # visited 배열 매 탐색마다 갱신 필요
    # 터트려서 새로운 배열 반환하는 함수 필요
# 시간복잡도

# 변수계획
# 뿌요시키는거 가능한 애들 표시한 stamp, visited, 

puyoMap = [list(input().rstrip()) for _ in range(12)]
ans = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def BFS (i,j,puyoMap,visited): 
    target = puyoMap[i][j]
    visited[i][j] = 1
    queue = deque()
    queue.append((i,j))
    temp = [(i,j)]
    count = 1
    while (queue):
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and puyoMap[nx][ny] == target and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                count += 1
                queue.append((nx,ny))
                temp.append((nx,ny))
    if count >= 4 : # 뿌요 성공
        for x in temp:
            i,j = x
            puyoMap[i][j] = '.'
        return True
    else : return False
def newPuyoMap (board) : # board에 1 표시된 애는 터트려야할 원소
    for j in range(6):
        for i in range(11,-1,-1):
            if board[i][j] == '.':
                for k in range(i-1,-1,-1):
                    if board[k][j] !='.':
                        board[i][j] = board[k][j]
                        board[k][j] = '.'
                        break
    return copy.deepcopy(board)

while(True):
    nextMapFlag = False
    currFlag = False
    for i in range(12):
        for j in range(6):
            if puyoMap[i][j] == '.': # 뿌요가능한 칸으로 표시해놓은 경우
                continue
            visited = [[0 for _ in range(6)] for _ in range(12)]
            currFlag = BFS(i,j,puyoMap,visited)
            if currFlag == True : nextMapFlag = True # 한번이라도 뿌요터짐
    if nextMapFlag == True :
        ans += 1
        puyoMap = newPuyoMap(puyoMap)
    elif nextMapFlag == False : break
print(ans)