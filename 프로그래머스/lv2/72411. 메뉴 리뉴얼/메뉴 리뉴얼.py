import copy
from itertools import combinations
def solution(orders, course):
    result = set()
    for menuLength in course :
        dict = {}
        for order in orders :
            newOrder = sorted(order,reverse=False)
            temp = []
            temp += combinations(newOrder,menuLength)
            if len(newOrder) < menuLength : continue
            for e in temp :
                x = ''.join(e)
                if dict.get(x) :
                    dict[x] += 1
                else: dict[x] = 1 # order 다 돌면서 사전 다 채움
            
        maxx = -100
        for key in dict.keys() :
            maxx = max(maxx,dict[key])
        if maxx < 2 :continue
        for key in dict.keys() :
            if dict[key] == maxx :
                result.add(key) 
                
    return sorted(list(result))