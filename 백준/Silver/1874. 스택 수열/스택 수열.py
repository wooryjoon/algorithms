import sys
input = sys.stdin.readline

# 기본 : 해당 수까지 push하고 pop
# input이 ans[-1]보다 작다면
# 	pop인데, stack[-1] != input이면
# 	fail

# input이 ans[-1]보다 크다면 
# 	해당 수까지 push하고 pop


n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = []
num = 1
flag = True
for e in arr :
    if not ans or e >= num :
        for x in range(num,e+1):
            stack.append(x)
            num += 1
            ans.append('+')
        stack.pop()
        ans.append('-')
    elif e < num :
        if stack[-1] != e:
            flag = False
            break  # 스택수열을 만들 수 없음
        stack.pop()
        ans.append('-')
if flag :print('\n'.join(ans))
else :print('NO')
