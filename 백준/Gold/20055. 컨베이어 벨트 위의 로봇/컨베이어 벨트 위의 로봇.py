import sys
input = sys.stdin.readline
from collections import deque
# 문제정리
# 벨트 한칸 회전 시 각 칸은 다음 위치로 이동, 끝칸은 첫 위치로 이동
# A[i] = i번 칸의 내구도
# 올리는 위치 : 첫칸
# 내리는 위치 : N번 칸
# 로봇은 첫칸에만 올릴 수 있음.
# 로봇이 내리는 위치 도달하면 즉시 내림
# 로봇은 스스로 이동도 가능
# 로봇을 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸이 내구도 1 감소

# 작동 규칙
### 전진 가능 조건 : 앞칸에 로봇x, 앞칸 내구도 1 이상 ###

# 벨트 전체 한칸 이동
# "내리는 칸" 에 로봇이 있다면 로봇 내림
# 벨트 위 "로봇"들이 순서대로 전진 가능하면 한칸 전진
# "내리는 칸" 에 로봇이 있다면 로봇 내림
# "올리는 칸" 의 내구도가 0이 아니면 로봇 올림
# 내구도가 0인 칸의 개수가 K 이상이면 과정 종료, else 다시 진행


N, K = list(map(int, input().split()))
life = deque(list(map(int, input().split())))
onRobot = deque([0] * 2 * N)
step = 0

def downRobot():
    if onRobot[N - 1] == 1: onRobot[N - 1] = 0  # 내리는 위치라면 내리기

def moveBelt():
    life.rotate()
    onRobot.rotate()

def robotMove():
    def moving(currBlock):
        nextBlock = (currBlock + 1) % (2 * N)
        if not onRobot[nextBlock] and life[nextBlock] >= 1:
            onRobot[nextBlock],onRobot[currBlock] = 1,0  # 로봇 이동
            life[nextBlock] = max(life[nextBlock] - 1, 0)  # 이동한 칸 내구도 감소

    for i in range(2 * N - 1, -1, -1):
        if onRobot[i] :  # 해당 칸에 로봇이 있으면
            moving(i)  #
            downRobot()

def upRobot():
    if life[0] > 0 and onRobot[0] == 0:
        onRobot[0] = 1
        life[0] = life[0] - 1

while True:
    step += 1
    moveBelt()
    downRobot()
    robotMove()
    upRobot()
    if life.count(0) >= K: break

print(step)