import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations,combinations

# n명은 짝수
# 1~N 번호부여
# 완탐?
# n명중에 n/2명을 조합으로 고른다.
# 각 case마다 차집합을 통해 상대팀을 구한다.
# 점수내는 함수로 점수 구하기
# diff 측정해서 minn 갱신
def sumScore (team,board):
    teamScore = 0
    for x in team :
        for y in team :
            teamScore += board[x][y]
    return teamScore
def sol () :
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    arr = set([i for i in range(n)])
    ans = float('inf')
    ways = list(combinations(arr,n//2))
    for x in ways :
        y = arr.difference(x)
        currDiff = abs(sumScore(x,board) - sumScore(y,board))
        ans = min(ans,currDiff)
    return ans


print(sol())