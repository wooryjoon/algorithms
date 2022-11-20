import sys
import heapq

input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort()

PQ = []

# 시작시간을 기준으로 첫번째 항의 종료시간을 먼저 PQ에 넣고, PQ는 종료시간을 기준으로 정렬
# 배열요소를 순차적으로 받으면서, 배열의 시작시간이 PQ의 첫항(최소힙정렬)보다 작으면 힙푸쉬.
# else, 힙팝후에 힙푸쉬
# 반복문이 모두 종료됬을 때 PQ의 길이를 답으로 제출
heapq.heappush(PQ,meetings[0][1])

for i in range(1,N):
    if meetings[i][0] < PQ[0]:
        heapq.heappush(PQ,meetings[i][1])
    else:
        heapq.heappop(PQ)
        heapq.heappush(PQ,meetings[i][1])

print(len(PQ))

