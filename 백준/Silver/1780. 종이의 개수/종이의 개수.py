import sys
input = sys.stdin.readline
"""
문제 정리
    재귀적으로 종이를 자르는 문제
    N은 3의 n승 꼴로 주어진다.
아이디어
    1. 현재 사각형의 모든 원소가 동일한지 확인
    2. 동일하지 않다면 9등분 해서 각각의 서브 사각형을 square로 하는 재귀함수 실행
    3. 동일하다면 return
풀이 방법
    1. 사각형의 동일성 체크 함수
    2. 0, -1, 1 의 각 개수를 카운팅하는 변수
"""
N = int(input())
init_square = [list(map(int,input().split())) for _ in range(N)]
minus_one = 0
zero = 0
plus_one = 0

def isAllSameElement(square) :
    target = square[0][0]
    # 하나라도 다른 원소가 있으면 return False
    for row in square :
        for e in row :
            if e != target :
                return False
    # 아니라면 return True
    return True
def count(num) :
    global plus_one
    global zero
    global minus_one

    if num == 1 :
        plus_one += 1
    elif num == 0:
        zero += 1
    elif num == -1 :
        minus_one += 1

def check(square) :
    if isAllSameElement(square):
        count(square[0][0])
        return
    else :
        # 9등분
        # (0,0) (0,3) (0,6) (3,0)
        length = len(square)
        child = length // 3
        if child == 0 : child = 1
        for i in range(3):
            for j in range(3):
                x = i * child
                y = j * child
                newArr = []
                for z in range(child):
                    newArr.append(square[x+z][y:y+child])
                check(newArr)

check(init_square)
print(minus_one)
print(zero)
print(plus_one)
