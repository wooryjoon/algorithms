import sys
from collections import deque
input = sys.stdin.readline

# [아이디어]
#스택으로 하나씩 쌓아가면서 기호에 따라 특정 연산?
# [시간복잡도]
# 선형탐색
# [변수 사용계획]
# 스택배열, 출력값을 담을 변수 , 
arr = list(input().strip())
stack = deque()
two = 0
three = 0
ans = 0
flag = 0
for x in arr :
    if x =='(' :
        two += 1
        stack.append(x)
    elif x == ')':
        if stack and stack[-1] == '[':
            print(0)
            flag = 1
            break
        if stack and stack[-1] == '(':
            two -= 1
            k = 1
            for _ in range(two):
                k *= 2
            for _ in range(three):
                k *= 3
            ans += k * 2
            
        else : two -= 1
        stack.append(x)
    elif x == '[' :
        three += 1
        stack.append(x)
    elif x ==']' : 
        if stack and stack[-1] == '(':
            print(0)
            flag = 1
            break
        if stack and stack[-1] == '[':
            three -= 1
            k = 1
            for _ in range(two):
                k *= 2
            for _ in range(three):
                k *= 3
            ans += k * 3
        else: three -= 1
        stack.append(x)
    if two <0 or three <0 : 
        print(0)
        flag = 1
        break

if flag == 0: 
    if two != 0 or three != 0 : print(0)
    else : print(ans)