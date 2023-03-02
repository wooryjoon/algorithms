import sys
input = sys.stdin.readline
from collections import deque

# 벨트의 한 위치부터 k개를 연속해서 먹으면 할인된 가격 제공
# 위 행사에 참여하는 경우, 초밥 종류 하나를 공짜로 먹을 수 있음.
# 즉, 쿠폰초밥은 제외하고서 k개를 먹을 수 

#초밥 종류를 최대로 하고 싶으므로 ㄴ행사참여가 이득.
# 즉 문제를 단순화하면,
#쿠폰초밥을 제외하고, k개를 연속으로 먹을때 먹는 가지수가 최대가 되도록.

# 7 9 7 30 -> 종류 3개.
# left + 1 right + 1
# 9 7 30 2 -> 
# arr[i % 초밥갯수]


# N : 접시 수, d : 초밥가짓수 k :연속해서 먹어야하는 길이, c : 쿠폰 번호 
[N,d,k,c] = list(map(int,input().split())) 
maxx = 1
sushiBelt = [int(input()) for _ in range(N)]
sushiVisited = [0] * (d+1)
sushiVisited[c] = 1 # 먼저 먹은 셈 친다.
# 최초 회전초밥 리스트

for i in range(k):
    currSushi = sushiBelt[i]
    if sushiVisited[currSushi] == 0 :
        maxx += 1
    sushiVisited[currSushi] += 1
left = 0
right = k-1
temp = maxx
while left < N :
    leftSushi = sushiBelt[left % N]
    sushiVisited[leftSushi] -= 1
    if sushiVisited[leftSushi] == 0 :
        temp -= 1
    left += 1
    right += 1
    nextSushi = sushiBelt[right % N]
    sushiVisited[nextSushi] += 1
    if sushiVisited[nextSushi] == 1 :
        temp += 1
    maxx = max(maxx,temp)
print(maxx)
