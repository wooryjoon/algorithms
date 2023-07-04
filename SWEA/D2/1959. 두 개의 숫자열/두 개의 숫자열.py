
from collections import deque
T = int(input())
ans = []
for test in range(1,T+1):
    N,M = list(map(int,input().split()))
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    answer = float('-inf')
    # 둘중에 길이가 짧은 애를 고정시켜야함
    if M < N :
        N,M = M,N
        arr1,arr2 = arr2,arr1
    arr2 = deque(arr2)
    while True :
        temp = 0
        for i in range(N):
            temp += arr1[i] * arr2[i]
        answer = max(answer,temp)
        arr2.popleft()
        if len(arr2) < N : break
    ans.append(answer)

for i in range(1,T+1):
    print(f"#{i} {ans[i-1]}")
