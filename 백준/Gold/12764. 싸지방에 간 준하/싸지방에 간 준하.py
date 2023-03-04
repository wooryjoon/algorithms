import sys
input = sys.stdin.readline
from collections import deque
from heapq import heappush,heappop, heapify,heappushpop
# 비어있는 자리 중에 번호가 가장 작은 자리에 앉는다.
# 모든 사람은 정해진 시간에 싸지바을 이용한다
# 모든 사람이 기다리지 않고 싸지방을 이용할 수 있는 컴퓨터의 최소 갯수
# 그 컴퓨터 대수에서 자리별로 몇명의 사람이 이용했는가
N = int(input())
computers = [0] *(N)
players = [list(map(int,input().split())) for _ in range(N)]
players.sort()
# 10 100 0
# 20 50 1
# 30 120 2
# 60 110 1
# 80 90 3
heap = []
pcHeap = [i for i in range(N)]
heapify(pcHeap)

for x in players:
    (start,end) = x
    if not heap :
        heappush(heap,(end,start,0))
        pcNumber = heappop(pcHeap)
        computers[pcNumber] += 1
        continue
        # start end 자리
    temp = heap[0]
    if start < temp[0] : # 애초에 다른자리 앉아아함
        pcNumber = heappop(pcHeap)
        computers[pcNumber] += 1
        heappush(heap,(end,start,pcNumber))
    else :
        while True : # 빈자리 다 빼주기
            prev_end,prev_start,prev_pc = heappop(heap)
            if heap and heap[0][0] <= start :
                heappush(pcHeap,prev_pc) # 사용 가능한 pc 목록에 추가
            else :
                pcNumber = heappushpop(pcHeap,prev_pc) # 사용가능한 애중에 제일작은놈
                computers[pcNumber] += 1
                heappush(heap,(end,start,pcNumber))
                break
ans = []
for x in computers :
    if x == 0 :
        break
    ans.append(x)
print(len(ans))
print(' '.join(map(str,ans)))
