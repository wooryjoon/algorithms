def solution(numbers):
    ans = [-1] * (len(numbers))
    stack = []
    for i in range(len(numbers)):
        currValue = numbers[i]
        while stack and stack[-1][0] < currValue:
            ans[stack[-1][1]] = currValue
            stack.pop()
        stack.append([numbers[i],i]) # 값과 인덱스
    return ans