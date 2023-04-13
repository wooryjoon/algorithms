def solution(d, budget):
    d.sort()
    ans = 0
    for i in range(len(d)):
        if budget >= d[i] :
            budget -= d[i]
            ans += 1
        else : break
    return ans