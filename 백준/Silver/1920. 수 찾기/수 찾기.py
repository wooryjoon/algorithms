import sys
from bisect import bisect_left,bisect_right, bisect
input = sys.stdin.readline
# 아이디어
# 비슷한 패턴. bisect로풀어보자
# 시간복잡도

# 변수계획

n = int(input())
A = list(map(int,input().split()))
m = int(input())
arr = list(map(int,input().split())) # 얘네들이 A에 존재하는지 확인
def solution (n,A,m,arr):
    ans = []
    A.sort()
    for x in arr:
        idx = bisect_left(A,x)
        if idx < n and A[idx] == x :
            print(1)
        else : print(0)
solution(n,A,m,arr)
