import sys
import copy
from collections import deque
input = sys.stdin.readline
# 아이디어
# 종료지점 기준 오름차순 정렬
# 완전히 포함되는 경우
# 아니라면 그대로 더하기만
# 시간복잡도
# 선형 탐색
# 변수 사용 계획
# dist , i

n = int(input())

lines = [list(map(int,input().split())) for _ in range(n)]
lines.sort(key = lambda x : (x[0],x[1])) # 배열의 두번째 원소를 기준으로 정렬

def solution (lines):
    dist = 0
    left = 0
    right = 0
    ans = 0
    for i in range(len(lines)) :
        x,y = lines[i]
        if i == 0 : # 초기값
            left = x
            right = y
            ans += y-x
            continue

        ans += y-x

        if x >= left and y <= right: # 포함되는 경우
            ans -= y-x
            continue
        if x <= right and y >= right :  # 걸치는 경우
            ans -= right - x
        
        left = x
        right = y
    return ans

print(solution(lines))
