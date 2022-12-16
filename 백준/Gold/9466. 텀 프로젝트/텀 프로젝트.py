# 사이클이 만들어져야 팀이된다.
# 자기자신 선택한경우 혼자서 팀
# 어디에도 속하지앟는 학생들의 수를 계산
import sys
sys.setrecursionlimit(10**6)

T = int(input())

def DFS (startNode) :
    target = maps[startNode]
    visited[startNode] = True
    if (visited[target]):
        if (target in arr): # 재귀 잘 돌다가 사이클 만들어지면, 그 사이클 애들 전부 1로바꾸고 나가리
            startIndex = arr.index(target)
            for i in range(startIndex,len(arr)):
                result.append(arr[i])
            return
    #수행 연산 
    else:
        arr.append(target)
        DFS(target)

for _ in range(T) :
    result = []
    n = int(input())
    maps = [0] + list(map(int,input().split()))
    visited  = [True] + [False for _ in range(n)] # 방문체크배열
    for j in range(1,n+1):
        if (visited[j] == True): continue
        arr = [j]
        DFS(j) # 각 노드에서 DFS돌리기
        
    print(n - len(result))