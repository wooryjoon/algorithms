import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    a, b = map(int,input().split())
    arr.append([a,b])

arr = sorted(arr, key=lambda x:x[0])

room = []
heapq.heappush(room,arr[0][1])
for i in range(1,n):
    if room[0] > arr[i][0]:
        heapq.heappush(room,arr[i][1])
    else : # 현재 회의실에서 바통터치 가능
        heapq.heappop(room)
        heapq.heappush(room,arr[i][1])

print(len(room))
