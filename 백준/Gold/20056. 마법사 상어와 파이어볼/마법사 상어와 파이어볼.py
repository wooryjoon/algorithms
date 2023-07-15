import sys
input = sys.stdin.readline

# N = board 크기
# M = 파이어볼 개수
# K = 이동 명령 횟수
# board의 시작과 끝은 연결되어 있음 N 이후에는 다시 0으로 돌아오는 구조
# board에 표시할 필요가 없는 문제
from collections import deque

N,M,K = list(map(int,input().split()))
board = [[deque() for _ in range(N)] for _ in range(N)]
fireball = deque()
dx = (-1,-1,0,1,1,1,0,-1)
dy = (0,1,1,1,0,-1,-1,-1)

for _ in range(M):
    # x, y, weight, direc, speed
    arr = list(map(int,input().split()))
    arr[1],arr[0] = arr[1]-1,arr[0]-1
    fireball.append(arr)

def moveFireBall(fireball):
    while fireball :
        #1 1 5 2 2
        #1 4 7 1 6
        x,y,w,s,d = fireball.popleft()
        # 이동 이후 위치 결정
        nx,ny = (x + dx[d] * s) % N, (y + dy[d] * s) % N
        board[nx][ny].append([nx,ny,w,s,d])

def spreadFireBall(fireball):
    def isAllSame(arr):
        odd = 0
        even = 0
        ans = len(arr)
        for e in arr :
            if e % 2 == 0 : even += 1
            else : odd += 1
        if odd == ans or even == ans : return True
        return False

    for i in range(N):
        for j in range(N):
            f_lengths = len(board[i][j])
            # 파이어볼이 2개 이상 -> 각 4개의 볼로 쪼개서 담기
            if f_lengths >= 2 :
                speed,weight,cnt,direction = 0,0,0,[]
                while board[i][j] :
                    x,y,w,s,d = board[i][j].popleft()
                    speed += s
                    weight += w
                    cnt += 1
                    direction.append(d)
                # make four ball
                nd = 0
                if isAllSame(direction): # 방향 0 2 4 6
                    nd = [0,2,4,6]
                else :
                    nd = [1,3,5,7]
                for dirs in nd:
                    # 유효한 fireball만 남기기
                    if weight // 5 > 0 :
                        fireball.append([i, j, weight // 5, speed//cnt, dirs])
            # fireball이 1개 -> 질량 조건 맞다면 그대로 담기
            if f_lengths == 1 :
                x,y,w,s,d = board[i][j].pop()
                if w > 0 : fireball.append([x,y,w,s,d])






while K:
    moveFireBall(fireball)
    spreadFireBall(fireball)
    K -= 1

ans = 0
for e in fireball :
    x,y,w,s,d = e
    ans += w
print(ans)
