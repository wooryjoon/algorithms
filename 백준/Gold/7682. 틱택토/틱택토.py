
# 최종 상태 : 꽉참 + X O 개수 동일
# 최종 상태 : 꽉안참 + 가로 세로 대각선 3개 갖춰짐
result = []

def count(arr):
    numX = 0
    numO = 0
    for e in arr :
        if e == 'X' : numX += 1
        if e == 'O' : numO +=1
    return [numX,numO]

def check(arr,target):
    # 행체크
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] == target :
            return True
    #열체크
    for i in range(3):
        if arr[0][i] == arr[1][i] == arr[2][i] == target :
            return True
    #좌상대각선
    if arr[0][0] == arr[1][1] == arr[2][2] == target:
        return True
    #우상대각선

    if arr[0][2] == arr[1][1] == arr[2][0] == target:
        return True
    return False

while True :
    arr = list(input().strip())
    if len(arr) == 3 : break
    numX,numO = count(arr)
    board = [[0] * 3 for _ in range(3)]
    for i in range(9):
        board[i // 3][i % 3] = arr[i]

    if numX - numO >=2 : result.append('invalid')
    elif numO > numX : result.append('invalid')
    elif numX == numO :
        # O가 승리한 경우만 유효
        if check(board,"O") and check(board,'X') == False :
            result.append('valid')
        elif check(board,'O') == False and check(board,'X') == False:
            if '.' in arr : result.append('invalid')
            else :result.append('valid')
        else : result.append('invalid')
    elif numX == numO + 1 :
        if check(board,'X') and check(board,'O') == False:
            result.append('valid')
        elif check(board,'X') == False and check(board,'O') == False :
            if '.' in arr : result.append('invalid')
            else :result.append('valid')
        else : result.append('invalid')


for e in result :
    print(e)