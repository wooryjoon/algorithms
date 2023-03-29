import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations

# 연산은 무조건 앞에서부터 진행한다.
# 나눗셈은 몫만 취한다.
# 음수를 양수로 나눌때는 양수로 바꾼뒤 몫연산을 하고 부모를 바꾼다.

# n개의 수로 이루어진 수열이 주어지고, n-1개의 연산자가 주어진다.
# n-1개의 연산자는 덧셈,뺄셈,곱셈,나눗셈 부호의 갯수이다.
# n개의 수 사이에 연산자를 집어넣는데, 최대값 최소값 구하기.
# 각 부호들을 적절히 수 사이에 위치하는 연산.
# n-1 길이의 배열을 만들고, 순열로 나올 수 잇는 모든 경우 계산하면 시간초과

# 아이디어
    # max min 변수를 만들고, 계속 갱신해줄 예정
    # ways_of_gererate 함수를 통해 만들어진 Case마다 반복문 시행
    # arr과 case를 연산하는 함수를 통해 curr값 도출
    # curr과 max min 연산 시행 

def extractCurr(arr,case) :
    ans = arr[0]
    for i in range(len(case)):
        x = case[i]

        if x == '+' :
            ans += arr[i+1]
        elif x == '-' :
            ans = ans - arr[i+1]
        elif x == 'x' :
            ans = ans * arr[i+1]
        elif x == '%':
            if ans < 0 :
                ans = -ans // arr[i+1]
                ans = -ans
            elif ans >= 0 :
                ans = ans // arr[i+1]
    return ans

N = int(input())

arr = list(map(int,input().split()))
generator = list(map(int,input().split())) # 덧,뺄,곱,나눗
generators = []
maxx = -1000
minn = float('inf')

for _ in range(generator[0]) :
    generators.append('+')
for _ in range(generator[1]) :
    generators.append('-')
for _ in range (generator[2]) :
    generators.append('x')
for _ in range(generator[3]) :
    generators.append('%')

ways_of_gen = list(permutations(generators,N-1))
ways_of_gen = list(set(ways_of_gen))
for case in ways_of_gen :
    curr = extractCurr(arr,case)
    maxx = max(maxx,curr)
    minn = min(minn,curr)

print(maxx)
print(minn)