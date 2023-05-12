import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 계단은 한칸 or 두칸 이동 가능
    # 그러나, 연속해서 세 계단을 모두 밟으면 안됨.
    # 마지막 도착 계단은 반드시 밟아야함

# 아이디어
    # i번째 계단에서 가는 경우 : i+1 or i+2
    # 만약에 i-1에서 i로 온 경우에는 i+1로 갈 수 없다.
    # d[i] = i번쨰 계단까지 밟은 값 합의 최대값
    # d[i] = d[i-1] + s[i] or d[i-2] + s[i]
#시간복잡도

n = int(input()) # 계단 수
s = [0] * 301

for i in range(1,n+1) :
    s[i] = (int(input()))

def solution(n,s) :
    d = [0] * 301
    d[1] = s[1]
    d[2] = max(s[2],s[1]+s[2])
    for i in range(3,n+1) :
        d[i] = max(d[i-3]+s[i-1]+s[i],d[i-2]+s[i])
    print(d[n])
solution(n,s)
