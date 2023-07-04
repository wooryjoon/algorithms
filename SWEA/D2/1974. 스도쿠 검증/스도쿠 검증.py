T = int(input())
ans = []

def check1(board,x) :
    SET = set()
    for e in board[x] :
        if e in SET :
            return False
        SET.add(e)
    return True

def check2(board,y):
    SET = set()
    for i in range(9):
        num = board[i][y]
        if num in SET :
            return False
        SET.add(num)
    return True

def check3(board,x,y):
    SET = set()
    for i in range(x,x+3):
        for j in range(y,y+3):
            num = board[i][j]
            if num in SET :
                return False
            SET.add(num)
    return True

for _ in range(T):
    board = [list(map(int,input().split())) for _ in range(9)]
    flag1 = True
    flag2 = True
    flag3 = True

    # 가로 체크
    for x in range(9):
        if not check1(board,x):
            ans.append(0)
            flag1 = False
            break
    if not flag1 : continue

    # 세로 체크
    for y in range(9):
        if not check2(board,y):
            ans.append(0)
            flag2 = False
            break
    if not flag2 : continue

    # 작은 사각형 체크
    for i in range(3):
        for j in range(3):
            if not check3(board,i*3,j*3) :
                flag3 = False
    if not flag3 :
        ans.append(0)
        continue

    ans.append(1)
for i in range(T):
    print(f"#{i+1} {ans[i]}")


