import sys
from bisect import bisect_left,bisect_right, bisect
input = sys.stdin.readline
# 아이디어

# 이미 꽂혀있는건 pass
# 안 꽂혀있을때
# 	- 멀티탭 구멍이 남으면 꽂고 pass
# 	- 멀티탭 구멍이 없으면
# 		꽂혀있는 애들 중 빈도수가 젤낮은거 빼기

# 시간복잡도

# 변수계획
# 빈도수 체크 배열 , 멀티탭 배열 
N,K = list(map(int,input().split())) # 구멍개수, 횟수
arr = list(map(int,input().split())) # 순서

def solution (N,K,arr):
    count = 0
    isUsed = []
    for i in range(K):
        currLight = arr[i]
        if currLight in isUsed: continue # 이미 꼽혀있는 물품이면 패스
        if len(isUsed) < N : # 구멍 다안채웟으면 채우기
            isUsed.append(currLight)
            continue
        else :
            targetLight = -1
            removeIdx = -1
            for j in range(len(isUsed)):
                adaptedLight = isUsed[j]
                if adaptedLight not in arr[i:]:
                    targetLight = adaptedLight
                    break
                elif arr[i:].index(adaptedLight) > removeIdx:
                    removeIdx = arr[i:].index(adaptedLight)
                    targetLight = arr[i:][removeIdx]
            count += 1
            isUsed.remove(targetLight)
            isUsed.append(currLight)
    return count

print(solution(N,K,arr))


