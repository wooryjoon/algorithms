import sys
from collections import deque, defaultdict
input = sys.stdin.readline
# 문제 정리
    # R : 배열에 있는 수의 순서를 뒤집는 함수
    # D : 첫번째 수를 버리는 함수 (배열이 빈 경우 에러 발생)

# 아이디어

# 시간복잡도

# 변수계획

T = int(input())
for _ in range(T):
    p = list(input().rstrip()) # 함수
    n = int(input()) # 배열의 길이
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0 :
        arr = deque()
    reverseCount = 0
    flag = False
    for x in p:
        if x == 'R':
            reverseCount += 1
        if x == 'D':
            if not arr:
                print('error')
                flag = True
                break
            else :
                if reverseCount % 2 == 0 :
                    arr.popleft()
                else: arr.pop()
                    
    
    if flag == False :
        if reverseCount % 2 == 0 :
            print('[' + ','.join(arr) + ']')
        else :
            arr.reverse()
            print('[' + ','.join(arr) + ']')

