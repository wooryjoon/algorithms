import sys
from collections import deque
input = sys.stdin.readline

# stack을 두개 만들어서 각각 관리
# 1. 소괄호를 닫을 때 스택이 비어있거나, 스택의 top이 대괄호이면 잘못된 문장이다.
# 2. 대괄호를 닫을 때 스택이 비어있거나, 스택의 top이 소괄호이면 잘못된 문장이다.
# 3. 열린 괄호가 닫힌 괄호보다 많이 등장한다. ( 마지막에 stack이 비어있지 않을 때 )

while (True):
    target = input().rstrip()# 각 줄의 문자열
    flag = 0
    if target =='.' : break
    stack = deque()
    for x in target:
        if x == '(' or x =='[': # 여는 괄호일때는 일단 넣어준다.
            stack.append(x)
        elif x ==')' or x == ']': # 닫는 괄호일때는 검사 필요
            if not stack: 
                print('no')
                flag = 1
                break
            if x ==')':
                if stack[-1] == '[':
                    print('no')
                    flag = 1
                    break
            elif x == ']':
                 if stack[-1] == '(':
                    print('no')
                    flag = 1
                    break
            stack.pop() # 짝이맞는 애들만 남은 시점이므로 pop만 해준다.
    if flag == 0: # 문자열 한줄을 전체 돌동안 no가 안돼었따
            if stack:
                print('no')
            else : print('yes')
