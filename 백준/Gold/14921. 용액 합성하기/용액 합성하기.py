import sys
input = sys.stdin.readline


# 문제정리
    # 두 용액을 혼합하면 특성값은 두 용액의 합이 된다.
    # 두개 골라서 0 에 가장 가까운 용액
    # 1번만 할 수 있다.
    # 두개 골라서 이분탐색
# 아이디어
    # min 변수 계속 갱신해주면서 찾기.
# 시간복잡도
    # 이분탐색으로 NlogN 처리 가능
    # 투포인터로도 해보자
# 변수 사용
    # left right mid minAns

N = int(input())
arr = list(map(int,input().split()))
left = 0
right = N-1
minAns = 999999999
while left < right :
    mid = (left+right) // 2
    midValue = arr[left]+arr[right]
    if abs(midValue) < abs(minAns):
        minAns = midValue
    if midValue < 0 :
        left += 1
    else : 
        right -= 1
        if midValue == 0 :
            break
print(minAns)