import sys
from bisect import bisect_left,bisect_right, bisect
input = sys.stdin.readline
# 아이디어
# 산성(양수) 알칼리(음수) 배열에서 세가지를골라서 0에 가장 가깝게 만들기
# 삼중 반복은 택도 없다. 1회반복 + 투포인터
# i + left + right 가 
# 시간복잡도
# 2n^2
# 변수계획
# 계속 갱신해줄 ans 배열 , left right 
N = int(input()) # 배열 길이
arr = list(map(int,input().split())) # 해당 배열
arr.sort() # 정렬

def solution (N,arr):
    ans = float('inf') # 무한대로 설정
    sumArray = []
    for i in range(N) :
        left = i+1
        right = N-1
        while (left < right):
            currSum = arr[i] + arr[left] + arr[right]
            if abs(ans) > abs(currSum):
                ans = currSum
                sumArray = [arr[i],arr[left],arr[right]]
            if currSum == 0:
                return sumArray
            elif currSum < 0 :
                left += 1
            elif currSum > 0 :
                right -= 1
    return sumArray

print(' '.join(map(str,solution(N,arr))))
                