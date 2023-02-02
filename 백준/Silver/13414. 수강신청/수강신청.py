import sys
import copy
from collections import deque
input = sys.stdin.readline
# 문제 정리
    # 문제를 역순으로 돌려놓고,hash[배열 원소]가 있으면 ans에 안넣음.
# 아이디어

# 시간복잡도
    # 선형 시간.?
# 변수계획
    # 최종 배열을 담을 ans, 그리고 hash맵

K,L = list(map(int,input().split())) # 수강가능인원, 클릭목록 길이

waitList = [input().rstrip() for _ in range(L)]
waitList.reverse()
hashMap = {}
ans = []
for x in waitList:
    if x in hashMap: continue
    hashMap[x] = True
    ans.append(x)

ans.reverse()
for i in range(min(len(ans),K)):
    print(ans[i])
