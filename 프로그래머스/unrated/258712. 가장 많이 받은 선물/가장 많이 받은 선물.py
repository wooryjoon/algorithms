def solution(friends, gifts):
    """
    A와 B간의 선물을 주고받는 규칙이 있다
    1. 두 사람이 선물을 주고받은 기록이 있다면, 이번 달 까지 더 많이 준 사람이 다음달에 선물을 받음
    2. 두 사람이 선물을 주고 받은 기록이 없거나, 주고 받은 수가 같다면, 선물 지수가 더 큰 사람이 선물을 받음
    *선물지수 : 이번달까지 (내가 준 선물 - 받은 선물)의 총 합
    3. 만약 선물 지수 까지 같으면 선물을 주고 받지 않는다.
    
    [풀이 방법]
    giftMember[alex][adam] = alex가 adam에게 준 선물의 개수
    giftIndex[alex] = alex의 선물 지수
    answer = dict()
    
    friends 배열을 순회하며 이중Dict 생성
    
    gifts 배열을 순회하면서,
    A,B = gift
    giftMember[A].add(B)
    
    """
    giftHistoryCount = dict()
    giftIndex = dict()
    answer = dict()
    for send in friends :
        giftHistoryCount[send] = dict()
        giftIndex[send] = 0
        answer[send] = 0
        for receive in friends :
            if send == receive : continue
            giftHistoryCount[send][receive] = 0
    
    for gift in gifts :
        A, B = gift.split(' ')
        giftHistoryCount[A][B] += 1
        giftIndex[A] += 1
        giftIndex[B] -= 1
        
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            A = friends[i]
            B = friends[j]
            # 양자 간 주고 받은 경우가 같거나, 둘다 0인 경우
            if giftHistoryCount[A][B] == giftHistoryCount[B][A]:
                # 선물 지수가 더 큰 사람이 받는다.
                if giftIndex[A] > giftIndex[B] :
                    answer[A] += 1
                elif giftIndex[A] < giftIndex[B]:
                    answer[B] += 1
            # 양자 간 거래 기록이 있는 경우
            else :
                if giftHistoryCount[A][B] > giftHistoryCount[B][A]:
                    answer[A] += 1
                elif giftHistoryCount[A][B] < giftHistoryCount[B][A] :
                    answer[B] += 1
    maxx = -1                
    for key in answer:
        maxx = max(maxx,answer[key])
    return maxx