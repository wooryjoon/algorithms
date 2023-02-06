import sys
from collections import deque, defaultdict
input = sys.stdin.readline
from heapq import heappop,heappush,heapify
# 문제 정리
    # x == 1: 어려운문제, 번호 큰거
    # x == -1 : 쉬운문제, 번호 작은거
    # add P L : 난이도가 L인 문제번호 P를 추가 ( P는 리스트에 없는거만 드렁옴)
    # solved P : 추천 리스트에서 문제번호 P를 제거한다.
# 아이디어
    # 최소힙,최대힙 활용해보자.
    # 10만개까지 문제개수, nlogn.
    # 삭제는 이분탐색
    # 각 리스트의 원소는 [난이도,문제번호] 순서로.
# 시간복잡도
    #nlogn
# 변수계획

N = int(input())
max_heap = []
min_heap = []
isSolved = defaultdict(bool)
for i in range(N):
    temp = (list(map(int,input().split())))
    isSolved[temp[0]] = False # 아직 안 품
    heappush(max_heap,(-temp[1],-temp[0])) # 음수부호로 최대힙 구현
    heappush(min_heap,(temp[1],temp[0]))

M = int(input())
for _ in range(M):
    inputs = list(input().split())

    if inputs[0] == 'add':
        isSolved[int(inputs[1])] = False
        heappush(max_heap,(-int(inputs[2]),-int(inputs[1])))
        heappush(min_heap,(int(inputs[2]),int(inputs[1])))
    elif inputs[0] == 'recommend':
        if inputs[1] == '1' : # 어려운 문제 추천
            while isSolved[-max_heap[0][1]]: # 이미 푼 거 다 없애놓고
                heappop(max_heap)
            print(-max_heap[0][1])
        elif inputs[1] == '-1' :
            while isSolved[min_heap[0][1]]:
                heappop(min_heap)
            print(min_heap[0][1])
    elif inputs[0] == 'solved':
            isSolved[int(inputs[1])] = True
            while isSolved[-max_heap[0][1]]:
                heappop(max_heap)
            while isSolved[min_heap[0][1]]:
                heappop(min_heap)