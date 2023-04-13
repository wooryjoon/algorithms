def solution(d, budget):
    d.sort()
    ans = 0
    for i in range(len(d)):
        x = d[i]
        if budget >= x :
            budget -= x
            ans += 1
        else : 
            break
    return ans