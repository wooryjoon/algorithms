import sys
input = sys.stdin.readline

T = int(input())
# 백스페이스 화살표 주의 , 스택으로 못푸나?
for _ in range(T): # 테케 두번 반복
    pwd = input().strip()
    left  = []
    right = []
    for x in pwd :
        if x =='<':
            if left :
                right.append(left.pop())
        elif x =='>':
            if right :
                left.append(right.pop())
        elif x =='-':
            if left:
                left.pop()
        else:
            left.append(x)
    print(''.join(left) + ''.join(reversed(right)))
