from collections import defaultdict
def solution(want, number, discount):
    # 할인품은 하루에 하나만 구매 가능
    # 10일간 회원자격
    # discount의 시작점 가능 범위 :  i ~ len(disc) - 10
    wantMap = defaultdict(int)
    answer = 0
    
    for i in range(len(want)):
        wantMap[want[i]] = number[i]
        
    for i in range(len(discount)-10+1):
        discountMap = defaultdict(int)
        for e in discount[i:i+10]:
            discountMap[e] += 1

        flag = False
        for e in want:
            if not discountMap.get(e) or wantMap[e] > discountMap[e]:
                flag = True
                break
        if not flag : answer += 1
    return answer