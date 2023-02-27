import sys
input = sys.stdin.readline
from collections import deque

# 문제 정리
    # 원래는 카드 순서대로 줘야하는데 사기침
    # 카드의 순서를 알고있으므로, 특정카드를 특정 선수수에게 주도록 할것
    # 카드를 섞을때는 주어진 방법대로 석을 수 있다.

# 아이디어
    # 목적 달성을 위해 카드 섞는 횟수의 최소값
    # N은 3~48
    # S를 한번, S를 두번, 반복~~~
    # S를 반복할 때 마다 카드의 위치가 P에 부합하는지?
    #   (0,0) (1,1) (2,2)
#시간복잡도

N = int(input()) # 카드 수, 플레이어는 3명이다.
P = list(map(int,input().split())) # 맨처음 i번쨰 카드를 p[i]에게 준다.
S = list(map(int,input().split())) # i번쨰 카드를 S[i]번째로 보낸다.

def solution (N,P,S) :
    dict = {}
    flag = False
    count = 0
    ans = ' '.join(map(str,P))
    newP = [i % 3 for i in range(N)] # 초기 i번카드는 newP[i]에게 간다.
    cardList = [i for i in range(N)]

    while True : # 카드 계속 섞기
        # 카드 정답 검사
        dictKey = ' '.join(map(str,newP))
        if dict.get(dictKey) : 
            print(-1)
            return
        if dictKey == ans:
            print(count)
            return
        dict[dictKey] = 1
        count += 1
        tempP = [0] * N
        tempC = [0] * N
        for i in range(N) : # 카드 섞기 시작
            currCardNumber = cardList[i] # 현재 처리할 카드 번호
            nextLoc = S[i] # 현재 카드리스트의 i번째에 존재하는 카드의 담위치
            tempC[nextLoc] = currCardNumber # 새로 만드는 카드리스트의 nextLoc에 현재카드 추가
            tempP[currCardNumber] = nextLoc % 3 # 현재 카드가 변화후에 몇P에게뽑히는가
        cardList = tempC
        newP = tempP
solution(N,P,S)