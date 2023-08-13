import sys
input = sys.stdin.readline


# N*N 보드 처음과 끝이 연결되어있음
# 최초 비바라기 시전 시 좌측 하단 4칸짜리 비바라기 생성
# 이동 명령
    # 구름이 방향에 따라 이동 (처음과 끝 연결)
    # 구름이 생기는 좌표를 list로 담기
    # 구름list를 돌면서 board[x][y] 증가
    # 구름list의 (x,y) 좌표 돌면서 추가 물 계산 (이때는 사이클 x)
    # if board[x][y] >= 2 and not in 구름list :
        # board[x][y] -= 2
        # newclouds.append((x,y))

# 입력
dx = (0,0,-1,-1,-1,0,1,1,1)
dy = (0,-1,-1,0,1,1,1,0,-1)
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
query = [list(map(int,input().split())) for _ in range(M)]

def move(clouds,d,s):
    newClouds = []
    for e in clouds :
        x,y = e
        nx,ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
        nx = (N + nx) if nx < 0 else nx
        ny = (N + ny) if ny < 0 else ny
        newClouds.append((nx,ny))
    return newClouds
# 최초 구름 init
clouds = []
for e in [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]:
    clouds.append(e)
# 구름 이동 명령 시작
for q in query :
    d,s = q
    # 구름이 d방향으로 s만큼 이동
    clouds = move(clouds,d,s)
    # 구름에서 비 내려서 구름 칸 증가
    for e in clouds :
        x,y = e
        board[x][y] += 1
    # 구름이 있던 칸 물복사 버그 시전
    for e in clouds :
        x,y = e
        cnt = 0
        # 대각선만 체크
        for i in [2,4,6,8]:
            nx,ny = x + dx[i], y + dy[i]
            # 사이클 형성 x -> 범위 제대로 잡아줘야함
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] > 0 : cnt += 1
        board[x][y] += cnt
    # board를 돌면서 새로운 구름 생성
    setClouds = set(clouds) # in 메서드를 빠르게 돌리기 위한 set 사용
    newClouds = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i,j) not in setClouds:
                newClouds.append((i,j))
                board[i][j] -= 2
    clouds = newClouds

ans = 0
for e in board :
    ans += sum(e)
print(ans)


