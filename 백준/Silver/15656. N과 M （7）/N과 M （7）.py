import sys
input = sys.stdin.readline

# 매일매일 
# 주식 하나 사거나, 원하는 만큼 팔거나, 아무짓도 안하거나 셋중 하나.

# 10 7 6 일때는 언제 사든 손해이므로 계속 가만있어야함
# 3,5,9 일때는 주식 사거나 팔면서 이익 실현 가능
# 최대이익 구하는 방법
# 뒤 원소부터 탐색 시작
# 앞으로 한칸씩 가면서 자기보다 값이 작은 원소면 차액을 더한다.
# 

n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
ans = []
def DFS(depth) :
    if depth == m :
        print(' '.join(map(str,ans)))
        return
    for x in arr :
        ans.append(x)
        DFS(depth+1)
        ans.pop()

DFS(0)