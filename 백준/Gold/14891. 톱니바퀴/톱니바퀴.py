import sys
from collections import deque
input = sys.stdin.readline
# 문제 정리
    # 8개의 톱니를 가진 4개의 바퀴. N극,S극 
    # 왼쪽톱니부터 1번 2번 3번 4번
    # 회전시킬땐 한칸씩 이동, 회전시킬 바퀴와 방향 정해야함
    # if 근처 바퀴가 회전할때 
    # 맞닿은 부분이 서로 같은 극이었다면 회전 x
    # 맞닿은 부분이 서로 다른 극이라면 옆 바퀴의 회전 방향과 반대로 회전
    # N극은 0, S극은 1로 나타남
    # 회전시킨 톱니바퀴 번호, 방향 (1은 시계방향, -1은 반시계 방향)
# 아이디어
    # k번을 반시계 돌린다
    # 양 옆 바퀴들 상태를 연쇄적으로 업데이트 (BFS?)
    # 톱니바퀴를 시계방향으로 돌리는 함수, 반시계로 돌리는 함수
    # 돌아갈 수 있는지 판단하는 함수
# 시간복잡도

# 변수계획
    # 양방향 탐색
dy = [1,-1]
circles = [False]
def rotate (circles,target,order):
    temp = deque(circles[target])
    if order == 1: # 시계방향, pop and shift
        temp.appendleft(temp.pop())
    elif order == -1: # 반시계방향 unshift and append
        temp.append(temp.popleft())
    circles[target] = list(temp)
def BFS (targetCircle,order,visited) :
    queue = deque()
    visited[targetCircle] = True
    queue.append([targetCircle,order])
    while queue:
        [currTarget,order] = queue.popleft()
        for i in range(2):
            sibling = currTarget + dy[i]
            if dy[i] == -1 and 1<=sibling<=4 and visited[sibling] == False : # 왼쪽 형제
                if circles[sibling][2] != circles[currTarget][6]:
                    # 서로 다른 극이므로 돌아간다. 방향 체크
                    queue.append([sibling,-order])
                    visited[sibling] = True
            elif dy[i] == 1 and 1<=sibling<=4 and visited[sibling] == False :
                if circles[sibling][6] != circles[currTarget][2] :
                    queue.append([sibling,-order])
                    visited[sibling] = True
        rotate(circles,currTarget,order) # 현재 바퀴 돌려주기


for _ in range(4):
    circles.append(list(input().rstrip()))
k = int(input())
for _ in range(k):
    targetCircle,order = list(map(int,input().split()))
    visited = [False] * (5)
    BFS(targetCircle,order,visited)
score = 1
ans = 0
for i in range(1,5):
    if circles[i][0] == '1':
        score = 1 * 2 **(i-1)
        ans += score
print(ans)