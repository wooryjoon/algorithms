import sys
input = sys.stdin.readline

# 아이디어
    # case 분류
    # 스택을 활용한 효율적 계산
# 변수 사용

n = int(input())
location = [list(map(int,input().split())) for _ in range(n)]
ans = 0
stack = [location[0][1]] 
if stack[-1] > 0 : ans += 1
for i in range(1,n):
    x,y = location[i]
    if y > stack[-1] : # prev보다 높이가 크다면 새 빌딩
        ans += 1
        stack.append(y)
    elif y < stack[-1] : # prev보다 높이가 작다면, 이전 건물 높이 확인 By 스택
        while True : # 이전 건물 중에 현재 건물보다 높이가 작/같 나오면 break 
            stack.pop()
            if not stack or stack[-1] <= y : break
        if not stack or stack[-1] < y : 
            if y :ans += 1
            stack.append(y)
print(ans)

