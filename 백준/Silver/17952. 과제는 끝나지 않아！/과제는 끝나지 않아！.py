import sys
input = sys.stdin.readline


# 아이디어
    
# 문제 정리
    # 과제는 최근 순서로 한다.
    # 받으면 바로 시작
    # 과제하는중에 새 과제가 나오면 새 과제 진행
    # 새 과제가 끝났으면 이전 과제를 이어서 한다.
    # 스택?
# 시간 복잡도
# 변수 사용 계획

N = int(input()) # 몇분
tasks = []
stack = []
ans = 0
for i in range(N): 
    temp = list(map(int,input().split()))
    tasks.append(temp)
# [a,b,c] = b점 만점인 과제가 나오고 푸는데 c분이 걸린다.

for i in range(len(tasks)) :
    x = tasks[i]
    if not stack:
        if x[0] == 1:
            [a,score,cost] = x
            stack.append([a,score,cost-1])
    elif stack :
        if x[0] == 0 :
            stack[-1][2] -= 1;
        else :
            [a,score,cost] = x
            stack.append([a,score,cost-1])

    if stack:
        if stack[-1][2] == 0 :
            ans += stack.pop()[1]
print(ans)
