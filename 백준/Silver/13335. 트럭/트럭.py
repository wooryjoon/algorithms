import sys
from collections import deque, defaultdict
input = sys.stdin.readline
# 문제 정리
    # 그리디 스멜
# 아이디어
    # 초를 ++하면서 while문
    # queue에 트럭을 넣은 채 출발 [차무게,현재 다리에서 위치]
    # 큐에 있는 애들만 한칸씩 전진
    # queue에 있는 투럭의 무게 + 대기중인 차 무게가 L보다 작으면 큐진입 가능
    # queue가 빌때까지.
# 시간복잡도

# 변수계획

n,w,L = list(map(int,input().split())) # 트럭 수,다리 길이, 다리 하중
truckWeight = deque(list(map(int,input().split())))
count = 0
queue = deque()
while True:
    # 큐에 아무것도 없을 때
    if not queue :
        queue.append([truckWeight.popleft(),1]) # 초기값 세팅
        count += 1
        continue
    newQueue = deque()
    for x in queue:
        x[1] += 1
        if x[1] <= w:
            newQueue.append(x)
    queue = newQueue # 다리 이동 갱신
    currWeight = 0
    for x in queue :
        currWeight += x[0]
    if truckWeight and currWeight + truckWeight[0] <= L:
        queue.append([truckWeight.popleft(),1])
    count += 1
    if not queue : break
print(count)