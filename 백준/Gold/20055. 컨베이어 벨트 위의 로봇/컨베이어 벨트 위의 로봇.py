import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
# 문제정리
    # 벨트 한칸 회전 시 각 칸은 다음 위치로 이동, 끝칸은 첫 위치로 이동
    # A[i] = i번 칸의 내구도
    # 올리는 위치 : 첫칸
    # 내리는 위치 : N번 칸
    # 로봇은 첫칸에만 올릴 수 있음.
    # 로봇이 내리는 위치 도달하면 즉시 내림
    # 로봇은 스스로 이동도 가능
    # 로봇을 올리거나, 로봇이 어떤 칸으로 이동하면 그 칸이 내구도 1 감소
    
    # 규칙
        # 1. 벨트 한칸 전진
        # 2. 벨트 위 로봇들이 순서대로 전진 가능하면 한칸 전진
        # 3. 전진 가능 조건 : 앞칸에 로봇x, 앞칸 내구도 1 이상
        # 4. 올리는위치 칸의 내구도가 0이 아니면 로봇 올림
        # 5. 내구도가 0인 칸의 개수가 K이상이면 과정 종료 or 다시 진행

# 아이디어
    # 순서대로 구현
# 시간복잡도

# 변수 사용 계획
N,K = list(map(int,input().split()))
arr = list(map(int,input().split()))
onRobot = [0] * 2*N
step = 0

def downRobot () :
    if onRobot[N-1] == 1 : onRobot[N-1] = 0 # 내리는 위치라면 내리기
def moveBelt (arr,onRobot) :
    arr.insert(0,arr.pop())
    onRobot.insert(0,onRobot.pop())
    downRobot()

def robotMove(onRobot,arr) :
    
    def moveRobot(curr) : 
        nextBlock = (curr+1)%(2*N)
        if onRobot[nextBlock] == 0 and arr[nextBlock] >= 1 :
            # 로봇 전진 가능
            onRobot[nextBlock] = 1 # 로봇 이동
            onRobot[curr] = 0 
            downRobot()
            arr[nextBlock] = max(arr[nextBlock]-1,0)  # 이동한 칸 내구도 감소
    
    
    for i in range(2*N-1,-1,-1):
        if onRobot[i] == 1 : # 해당 칸에 로봇이 있으면
            moveRobot(i) # 


def upRobot (arr,onRobot) :
    if arr[0] > 0 and onRobot[0] == 0 : 
        onRobot[0] = 1
        arr[0] = arr[0]-1






while (True) :
    step += 1

    moveBelt(arr,onRobot)

    robotMove(onRobot,arr)

    upRobot(arr,onRobot)

    cnt = 0
    
    for e in arr :
        if e == 0 :
            cnt += 1
    if cnt >= K : break

print(step)