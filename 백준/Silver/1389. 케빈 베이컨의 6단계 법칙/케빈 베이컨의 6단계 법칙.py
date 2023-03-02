import sys
input = sys.stdin.readline
from collections import deque

# 케빈베이컨 : 단계의 총합이 가장 적은 사람
# 유저들간 케빈베이컨중 가장 적은 사람
# 플로이드 워셜
N,M = list(map(int,input().split()))
board = [[float('inf')] * N for _ in range(N)]
for _ in range(M):
    a,b = list(map(int,input().split()))
    board[a-1][b-1] = 1
    board[b-1][a-1] = 1

for i in range(N):
    for j in range(N):
        if i == j :
            board[i][j] = 0 # 자기자신에게 가는건 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            board[i][j] = min(board[i][j],board[i][k]+board[k][j])
ans = float('inf')
result = []
for i in range(N):
    result.append((sum(board[i]),i)) # 합과 인덱스넘버

result.sort(key = lambda x:(x[0],x[1]))
print(result[0][1]+1)