from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

ans = []

for _ in range(N//4):
    ans.append("long")
ans.append("int")

print(' '.join(ans))