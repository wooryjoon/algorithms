def solution(board, moves):
# [0,0,0,0,0],
# [0,0,1,0,3],
# [0,2,5,0,1],
# [4,2,4,4,2],
# [3,5,1,3,1]
    # 배열 돌리고 스택.
    newBoard = []
    stack = []
    ans = 0
    
    # 배열 돌리기
    for i in range(len(board[0])):
        temp = []
        for j in range(len(board)-1,-1,-1):
            if board[j][i] != 0:
                temp.append(board[j][i])
        newBoard.append(temp)
        
    # moves 배열 따라 움직이기
    for e in moves:
        currIdx = e-1
        if not newBoard[currIdx] : continue # 칸이 빈 경우 패스.
        value = newBoard[currIdx].pop() # 뽑기
        if not stack : stack.append(value) # 스택이 비어있다면 하나 넣기
        else :
            if stack[-1] == value : # 값이 같다?
                ans += 2
                stack.pop()
            else : # 값이 다르다?
                stack.append(value)
    return ans
                

    