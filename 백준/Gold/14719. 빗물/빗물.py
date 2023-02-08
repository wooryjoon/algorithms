import sys
input = sys.stdin.readline
# 문제 정리
    # 문제에서 요구하는 대로 2차원 배열 만든다.
    # 만든 2차원 배열을 이중 반복하며 특정한 조건에 따라 빗물 칸을 카운트한다.
    # 특정한 조건은 아래 코드에서 알려드림

H,W = list(map(int,input().split())) # 세로,가로 입력 받기
blocks = list(map(int,input().split())) # 각 세로 줄에 블록이 쌓인 높이
board = [[0 for _ in range(W)] for _ in range(H)] # 2차원 배열 만들 틀

for i in range(W):
    for j in range(H-1,H-blocks[i]-1,-1):
        board[j][i] = 1 # blocks 값에 따라 문제의 그림처럼 배열을 만든다.
        # board[3][0] = 1
        # board[2][0] = 1
        # board[1][0] = 1
        # 이런 식으로 채워지는 반복문임

count = 0 # 정답으로 출력할 변수
for arr in board : # 2차원 배열 반복문
    oneFlag = False # 각 행을 차례대로 탐색하면서, 블록이면 True로 변환
    water = 0 # 각 행의 빗물 칸의 개수 
    for i in range(len(arr)):# 각 행 배열 반복문
        x = arr[i]
        # oneFlag가 True일때 빗물칸을 카운트하고
        # oneFlag가 True인 상태에서 그 다음 블록을 만나면, 그 빗물칸은 유효한 칸
        # 그러므로 count에 water를 더해준다
        # 만약에 oneFlag가 False이거나, oneFlag가 True인데 블록을 못만나고 종료되면
        # 유효한 빗물이 아니므로 더해주지 않는다.
        if x == 1 : 
            if oneFlag == False :
                oneFlag = True
            if oneFlag == True :
                count += water
                water = 0
            continue
        if x == 0 :
            if oneFlag == True :
                water += 1
            continue
print(count)