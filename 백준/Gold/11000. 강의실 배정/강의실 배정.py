import sys
import heapq
input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

# 시작시간을 기준으로 소팅
time = sorted(time, key=lambda x:x[0])

q = []
first= time.pop(0)
heapq.heappush(q, first[1])

for i in time:
    #print(i)
    if q[0] <= i[0]:
        heapq.heappop(q)
        heapq.heappush(q, i[1])
    else:
        heapq.heappush(q, i[1])

print(len(q))