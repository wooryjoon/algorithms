import sys
input = sys.stdin.readline
import copy

# 아이디어
    # n개중 1개 뽑을 수 있는 모든 case를 돌며 조건 만족하는지 확인
    # ... 
    # n개중 n개 뽑을 수 있는 모든 case를 돌며 조건 만족하는지 확인
    # 위 반복문을 돌며 ans값 최대값으로 계속 갱신

# 풀이 과정
    # 1부터 n까지 i로 반복문
    # cases = [combination(arr,i)]
        # cases 돌면서 각 케이스 돌기
            # e = ((1,3),(2,1),(3,5))
            # check(e) == true ?
            # ans = max(ans,i) break
    #print(ans)

# 시간초괴

# 새로운 풀이
    # 
def sol() :
    n = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [0] *(n+1)
    global ans
    ans = 0
    ansArr = []

    def DFS(start,curr,arr) :
        global ans
        for e in graph[curr] : # curr에서 갈 수 있는 노드탐색
                if visited[e] == 0 :
                    visited[e] = 1
                    arr.append(e)
                    DFS(start,e,arr)
                    arr.pop()
                    visited[e] = 0
                if e == start :
                    ans += len(arr)
                    for e in arr :
                        ansArr.append(e)
                    return 

    for i in range(n):
        v = int(input())
        graph[i+1].append(v)

    for i in range(1,n+1):
        visited[i] = 1
        DFS(i,i,[i])
    print(ans)
    print('\n'.join(map(str,sorted(ansArr))))
sol()