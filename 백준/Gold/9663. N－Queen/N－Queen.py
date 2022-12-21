N = int(input()) # N * N 체스판 
# N = 8
cnt = 0

isusedY = [0 for i in range(N)]
rightCross = [0] * 2*N # 2n-1칸
leftCross = [0] * 2*N

def DFS (x):
    global cnt
    # 종료조건
    if (x == N):
        cnt  = cnt + 1
       
        return
    #수행연산
    for i in range(N):
        if (isusedY[i] == 0 and 
        rightCross[x+i] == 0 and 
        leftCross[x-i+N-1]== 0): # 사용되지않은 행이고, 이전점들의 대각선에 걸리지안흥ㅁ
            isusedY[i] = 1
            rightCross[x+i] = 1
            leftCross[x-i+N-1] = 1
            DFS(x+1)
            isusedY[i] = 0
            rightCross[x+i] = 0
            leftCross[x-i+N-1] = 0


DFS (0)
print(cnt)