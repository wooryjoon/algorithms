import sys
input = sys.stdin.readline
from collections import deque

# 서류성적과 면접성적 둘 다 다른애들보다 뒤쳐지면 탈락
# 2점 3점
# 4점 1점
# 1점 4점
# 3점 2점
# 0점 0점


# 최대 인원수 : 0명 ~ 지원자 
# 오름차순 정렬

# 0 0
# 1 4
# 2 3
# 3 2
# 4 1

# 스택으로 들어가면, 첫항은 당연히 더 클테니 두번째 항의 크기를 본다.
# stack[-1]의 두번째 항이 진입 두번째 항보다 작으면 +1 (실패자)

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    # for i in range(n):
    #     x,y = arr[i]
    #     arr[i] = n-x,n-y # 점수화
    # arr.sort()
    # cnt = 0
    # for i in range(n-1):
    #     if arr[i][1] < arr[i+1][1] : # 점수가 둘다 작다
    #         cnt += 1
    # print(n-cnt)
    arr.sort()
    # 순서대로 순회할 때, 이미 [0]은 앞자리 놈보다 작다.
    # 그러면 [1]이 앞자리 놈보다 커야한다.
    cnt = 0
    minn = arr[0][1]
    for i in range(1,n):
        if arr[i][1] > minn  :
            cnt += 1
        minn = min(minn,arr[i][1])
    print(n-cnt)


