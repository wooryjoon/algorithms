import sys
from collections import deque
input = sys.stdin.readline

wheels = [deque(list(input().strip())) for _ in range(4)]

K = int(input())

def rotate(wheel,dir):
    if dir == -1:
        wheels[wheel].append(wheels[wheel].popleft())
    if dir == 1 :
        wheels[wheel].appendleft(wheels[wheel].pop())


def BFS(wheel,dir) :
    visited= [0] * 4
    visited[wheel] = 1
    q = deque()
    q.append((wheel,dir))

    while q :
        wheel,dir = q.popleft()
        for i, nextWheel in enumerate([wheel-1,wheel+1]):
            if 0 <= nextWheel < 4 :
                # 왼쪽 확인
                if i == 0 :
                    if visited[nextWheel] == 0 and wheels[nextWheel][2] != wheels[wheel][6]:
                        visited[nextWheel] = 1
                        q.append((nextWheel,dir * -1))

                # 오른쪽 확인
                if i == 1:
                    if visited[nextWheel] == 0 and wheels[nextWheel][6] != wheels[wheel][2]:
                        visited[nextWheel] = 1
                        q.append((nextWheel, dir * -1))
        rotate(wheel, dir)

for _ in range(K):
    wheel,dir = list(map(int,input().split()))
    wheel -= 1
    BFS(wheel,dir)

ans = 0
for i, wheel in enumerate(wheels) :
    if wheel[0] == '1' :
        # N극
        ans += 2**i
print(ans)

