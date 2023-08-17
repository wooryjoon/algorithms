import sys
from collections import deque, defaultdict

input = sys.stdin.readline
# 문제 정리
# 처음엔 주사위에 모두 0
# 주사위 굴려서 온 칸에 쓰인 수가 0이면 주사위 바닥에 쓰인 수가 지도칸에 복사됨
# 0이 아니면 칸에 쓰인 수가 주사위 바닥에 복사되고 칸에 쓰인게  0으로 변함
#
# 아이디어
# 남쪽으로 이동
# 바닥 = 6 -> 5번
# 상단 = 1 -> 2번
# 북쪽으로 이동
# 바닥 = 6 -> 2번
# 상단 = 1 -> 5번
# 서쪽으로 이동
# 바닥 = 6 -> 4
# 상단 = 1 -> 3
# 동쪽 이동
# 바닥 : 6 -> 3
# 상단 : 1 -> 4

# 방향따라 주사위 각 좌표의 값을 갱신해주는 함수
# 주사위 굴릴때마다 board값 갱신, 주사위 값 갱신, 상단값 출력
# 지도 바깥으로는 나갈 수 없다.
# 시간복잡도

# 세로 가로 x좌표 y좌표 명령 갯수
N, M, x, y, K = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
order = list(map(int, input().split()))
# 주사위 전개도
# 0 2 0
# 4 6 3
# 0 5 0
# 0 1 0
dice = [0, 0, 0, 0, 0, 0, 0]


def diceRotate(k):
    prev = dice.copy()
    if k == 1:  # 동쪽이동
        dice[1] = prev[4]
        dice[3] = prev[1]
        dice[4] = prev[6]
        dice[6] = prev[3]
    elif k == 2:  # 서쪽 이동
        dice[1] = prev[3]
        dice[3] = prev[6]
        dice[4] = prev[1]
        dice[6] = prev[4]
    elif k == 3:  # 북쪽 이동
        dice[1] = prev[5]
        dice[2] = prev[1]
        dice[5] = prev[6]
        dice[6] = prev[2]
    elif k == 4:  # 남쪽 이동
        dice[1] = prev[2]
        dice[2] = prev[6]
        dice[5] = prev[1]
        dice[6] = prev[5]


for k in order:
    if k == 1:  # 동쪽
        nx, ny = x, y + 1
    elif k == 2:  # 서쪽
        nx, ny = x, y - 1
    elif k == 3:  # 북쪽
        nx, ny = x - 1, y
    elif k == 4:  # 남쪽
        nx, ny = x + 1, y

    if 0 <= nx < N and 0 <= ny < M:  # 좌표가 지도 범위 내
        # 주사위 굴리기
        diceRotate(k)
        if board[nx][ny] == 0:
            board[nx][ny] = dice[6]
        else:
            dice[6] = board[nx][ny]
            board[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])