import sys
input = sys.stdin.readline

# 아이디어
    # case 분류
        # 다음 빌딩이 현재 빌딩 높이보다 크면?
            # 무조건 새 빌딩이 하나 있다.
        # 다음 빌딩이 현재 빌딩 높이보다 작으면?
            # 이전 건물들의 높이를 쭉 보면서, 얘가 이미 있는 빌딩인지, 아닌지 판단

n = int(input())
location = [list(map(int,input().split())) for _ in range(n)]
ans = 0 
stack = []

for i in range(0,n):
    x,y = location[i]

    if not stack :
        if y != 0 : ans += 1
        stack.append(y)
        continue

    if y > stack[-1] : 
        ans += 1 
        stack.append(y)
        continue

    if y < stack[-1] : 
        while stack and stack[-1] > y : 
            stack.pop()
        if not stack or stack[-1] < y : 
            if y :ans += 1
            stack.append(y)
print(ans)