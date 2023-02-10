import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))
arr = list(map(int,input().split()))
sumArr = [0] * (N+1)
sumArr[1] = arr[0]
for i in range(1,N):
    sumArr[i+1] = sumArr[i] + arr[i]
for _ in range(M) :
    start,end = list(map(int,input().split())) 
    ans = sumArr[end] - sumArr[start-1]
    print(ans)
