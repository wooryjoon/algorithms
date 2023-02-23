import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 걷기 : 한칸뒤로 or 한칸 앞으로
    # 순간이동 : 2배 거리 이동
    # 수빈이는 동생을 찾고싶다. 가장 빠른 시간내에 찾는 방법구하기 (시간)
    
# 아이디어
    # BFS완탐으로 매 초에 갈 수 있는 모든 case 파악해보자?
# 변수
    # ans

N,M = list(map(int,input().split()))
visited = {}
visited[N] = 1
MAX = 100001
def BFS (start) :
    q = deque()
    q.append([start,0]) # 현재위치,초
    while q:
        curr,sec = q.popleft()
        if curr == M:
            return sec
        for i in [curr,1,-1] :
            nextCurr = curr + i # 한칸빼기, 한칸더하기, 두배로가기
            if nextCurr >= 100001 : continue
            if visited.get(nextCurr) : continue
            visited[nextCurr] = 1
            q.append([nextCurr,sec+1])
print(BFS(N))