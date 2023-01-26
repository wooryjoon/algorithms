import sys
from collections import deque
input = sys.stdin.readline

#[문제 정리]
# 암호 : 최소 모음1개, 최소 자음 2개 총 서로다른 L개
# 암호는 오름차순 추측 ( == 가능성 있는 암호)
# C개의 문자 후보를 통해서 가능성 있는 암호를 모두 구하라.

# [아이디어]
# 배열을 오름차순으로 정렬
# L개에서 멈추고 출력한다. DFS백트래킹
# 그런데, 배열은 최소 하나의 모음이 있어야 한다.
# [시간복잡도]

# [변수 사용계획]
# ??

L,C = list(map(int,input().split()))
alphabets = list(input().rstrip().split())
alphabets.sort()


def DFS(arr,depth,startIndex) :
    if depth == L :
        odd = 0
        even = 0
        for x in arr :
            if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o' :
                odd += 1
            else: even += 1
        if odd >= 1 and even >= 2 : print(''.join(map(str,arr)))    
        return
    else:
        for i in range(startIndex,C):
            arr.append(alphabets[i])
            DFS(arr,depth+1,i+1)
            arr.pop()
DFS([],0,0)


