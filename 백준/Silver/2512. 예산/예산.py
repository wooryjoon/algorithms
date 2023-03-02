import sys
input = sys.stdin.readline
from collections import deque

# 모든 요청을 그대로 수용가능하면 그대로
# 근데 예산 초과되면 일정 기준 정하고 그 기준 이상인 애들한테는 상한액 지급


N = int(input()) # 지자체 수
request = list(map(int,input().split())) #지자체별 요구사항
total = int(input()) # 총 예산
request.sort()
result = 0
if sum(request) <= total :
    print(max(request))
else :
    # 상한액을 최대한 높인다. 
    # 상한액 가능 범위는 뭐 min(r) ~ max(r) 일텐데, 이분탐색 가능할듯
    left = 0
    right = request[N-1]
    maxx = -100000
    while left <= right :
        currSum = 0
        mid = (left + right) // 2
        
        for x in request : # mid를 토대로 상한액 계산
            if x >= mid : # 상한액 이상인 요청 금액
                currSum += mid
            else :
                currSum += x
        if currSum <= total :
            left = mid + 1
            result = mid
        else : # 현재 상한액으로 헀을때 합이 total보다 크면 같다.
            right = mid - 1
    print(result)
