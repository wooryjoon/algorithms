# 수열 : 순서가 중요.  -> 1,3,2 와 1,2,3은 다른 것.-> 각 재귀에서 체크한 visited를 false로 바꿔준다

[N,M] = list(map(int,input().split()))
numArray = [] # 1,2,3
visited = [0]

for i in range(1,N+1):
    numArray.append(i); # 1부터 N까지의 수를 담은 배열 생성
    visited.append(False) # 1~N까지의 방문 배열 생성

def DFS(perm,visit,depth):
    # 종료조건
    if (depth == M):
        print(' '.join(map(str,perm)))
        return
    #수행연산
    for i in numArray:
        if(visit[i] == False):
            perm.append(i)
            visit[i] = True
            DFS(perm,visit,depth+1)
            visit[i] = False
            perm.pop()


DFS([],visited,0)
