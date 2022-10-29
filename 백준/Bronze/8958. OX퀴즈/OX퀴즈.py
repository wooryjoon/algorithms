#N만큼 반복하는 반복문 내에서, 각 케이스의 입력을 배열로 만듬,
#score 변수를 선언해 O가 나오는 규칙대로 score 를 계산하고 바로 출력
# 배열을 순회하면서 O이면 zerocount +1
# X이면 zerocount = 0 로
N = int(input())
List = []
score = 0
zeroCount = 0

for i in range(N) :
    zeroCount = 0
    score = 0
    List = list(input())
    for k in List :
        if k == 'O' :
            zeroCount += 1
        else :
            zeroCount = 0
        score += zeroCount
    print(score)    
