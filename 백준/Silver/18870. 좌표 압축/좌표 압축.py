import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리

# 아이디어
    #  각 값에 인덱스를 연결한 튜플로 값을 저장
    # (2,0) (4,1) (-10,2) (4,2) (-9,3)
    # 오름차순 정렬
    # (-10,2) (-9,3) (2,0) (4,1) (4,2)
    # if bisect_left-bisect_right = 0 :
    # 

# 변수

#시간복잡도
    # N * 

N = int(input())
arr = list(map(int,input().split()))
dict = {}
ans = []
arr2 = list(sorted(set(arr)))

for i in range(len(arr2)) :
    dict[arr2[i]] = i 

for x in arr :
    ans.append(dict[x])

print(' '.join(map(str,ans)))
