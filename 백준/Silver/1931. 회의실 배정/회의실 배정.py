import sys
import copy
from collections import deque
input = sys.stdin.readline
#아이디어
# 그리디, 종료시간 기준 오름차순 정렬
# while문으로 포인터 하나 설정해서 currEnd보다 작으면 pass, 크면 그거 넣기
# 시간복잡도
# 선형시간
# 변수 사용 계획
# count , i
# n = int(input()) # 계단 갯수
n = int(input())
meetings = []
for _ in range(n):
    meetings.append(list(map(int,input().split())))
meetings.sort(key=lambda x : (x[1],x[0]))

def solution (meetings,n) :
    ans = []
    for x in meetings:
        if not ans :
            ans.append(x)
        else :
            if ans[-1][1] <= x[0]:
                ans.append(x)
    return len(ans)
print(solution(meetings,n))