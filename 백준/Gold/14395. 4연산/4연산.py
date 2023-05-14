import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

s,t = list(map(int,input().split()))
def BFS():
    gen = ['*','+','-','/']
    visited = set()
    q = deque()
    q.append([s,''])
    visited.add(s)
    while q :
        num,ans = q.popleft()
        if num > 10**9 : continue
        if num == t :
            return ans
        for i in range(4):
            currGen = gen[i]
            nextNum = num
            if currGen == '*':
                nextNum *= num
            if currGen == '+':
                nextNum += num
            if currGen == '-':
                nextNum -= num
            if currGen == '/' and num != 0:
                nextNum = 1
            if nextNum in visited : continue
            visited.add(nextNum)
            q.append([nextNum,ans+currGen])
    return -1

if s == t :
    print(0)
    exit()
print(BFS())