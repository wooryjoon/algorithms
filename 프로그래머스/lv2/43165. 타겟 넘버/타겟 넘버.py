def solution(numbers, target):
    length = len(numbers)
    global ans
    ans = 0
    def DFS(num,depth) :
        global ans
        if depth == length :
            if target == num :
                ans += 1
            return
        DFS(num+numbers[depth],depth+1)
        DFS(num-numbers[depth],depth+1)
    DFS(0,0)
    return ans