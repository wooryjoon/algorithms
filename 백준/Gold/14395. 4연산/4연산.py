import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

s,t = list(map(int,input().split()))
def BFS():
    gen = ['*','+','-','/']
    visited = defaultdict(int)
    q = deque()
    q.append([s,''])
    visited[s] = 1
    while q :
        num,ans = q.popleft()
        if num > 10**9 : continue
        if num == t :
            return ans
        for i in range(4):
            currGen = gen[i]
            if currGen == '*':
                if visited[num*num] == 1 : continue
                if num*num > 10 ** 9: continue
                visited[num*num] = 1
                q.append([num*num,ans+currGen])
            if currGen == '+':
                if visited[num+num] == 1 : continue
                visited[num + num] = 1
                q.append([num+num,ans+currGen])
            if currGen == '-':
                if visited[num-num] == 1 : continue
                visited[num - num] = 1
                q.append([num-num,ans+currGen])
            if currGen == '/' and num != 0:
                if visited[num//num] == 1 : continue
                visited[num // num] = 1
                q.append([num//num,ans+currGen])
    return -1

if s == t : print(0)
else:
    print(BFS())