import sys
input = sys.stdin.readline


# 문제정리
    # 뱀 이동, 오른쪽을 우선으로 움직인다
    # 사과가 있다면 사과 먹고 꼬리 안줄임
    # 뱀이 벽또는 몸과 부딪히면 게임이 끝난다

# 아이디어
    # 매초마다 한번의 이동
    # 특정한 초에는 방향을 바꾼다.
    # 0,0에서 출발해서 오른쪽으로 이동.
    # 이동한 칸에 사과가 있다면 몸길이 + 1
    # 이동한 칸에 사과가 없다면  몸길이 그대로
    # 각 
    # while문.

# 시간복잡도

# 변수 사용
from collections import deque

n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 2

l = int(input())
dirDict = dict()
queue = deque()
queue.append((0, 0))

for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

def turn(alpha):
    global direction
    if alpha == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if graph[x][y] == 2:
        graph[x][y] = 1
        queue.append((x, y))
        if cnt in dirDict:
            turn(dirDict[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 1
        queue.append((x, y))
        tx, ty = queue.popleft()
        graph[tx][ty] = 0
        if cnt in dirDict:
            turn(dirDict[cnt])

    else:
        break

print(cnt)