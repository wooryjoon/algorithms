import sys
import copy
from collections import deque
input = sys.stdin.readline

#[문제 정리]
#올바른 모눈종이만 주어진다 -> 쓸데없는 칸없다.
# 주어진 박스안에 1. 위쪽 2. 왼쪽 
# [아이디어]
# 1. 이중반복을 하며 스티커를 노트북에 붙일 수 있으면 붙인다.
# 2. 만약 전혀 스티커를 못붙였다면 스티커를 90도 회전시켜서 다시 반복
# 3. 90도꺾기를 4번했는데도 안되면 스티커 버리고 다음걸로 간다.
# 4. 이렇게해서 스티커를 다 붙이고 빈칸의 개수 출력
# [시간복잡도]

# [변수 사용계획]
# 변화 후 x = 변화 전 y
# 변화 후 y = 변화 전 x축의 길이 - (x+1) 

N,M,K = list(map(int,input().split())) # 세로/가로/스티커개수
ansMap = [[0 for _ in range(M)] for _ in range(N)]
stickers = []
for _ in range(K):
    x,y = list(map(int,input().split()))
    stickers.append([list(map(int,input().split())) for _ in range(x)])



def patchable (x,y,sticker) : # 스티커를 붙이는 함수
    #x,y,를 시작점으로 스티커 붙이기
    for i in range(len(sticker)): # 스티커의 크기만큼 반복
        for j in range(len(sticker[i])):
            if i+x >=N or j+y >= M :return False
            if sticker[i][j] == 1 and ansMap[i+x][j+y] == 1:
                return False
    return True
def patch (x,y,sticker) :
    for i in range(len(sticker)): 
        for j in range(len(sticker[i])):
            if sticker[i][j] == 1:
                ansMap[i+x][j+y] = 1

def rotate_90 (sticker) :
    x = len(sticker)
    y = len(sticker[0])
    newSticker = [[0 for _ in range(x)] for _ in range(y)] # 가로세로 체인지
    for i in range(x) :
        for j in range(y) :
            newSticker[j][x-(i+1)] = sticker[i][j]
    return newSticker


for q in range(K): # 스티커 하나씩 잡기
    sticker = stickers[q]
    rotate_count = 0
    flag = False
    while (rotate_count <4) :
        for i in range(N) :
            for j in range(M) :
                if patchable(i,j,sticker) :
                    flag = True # 붙이면 True
                    patch(i,j,sticker)
                    break
            if flag : break
        if flag : break
        else: 
            sticker = rotate_90(sticker)
            rotate_count += 1

ans = 0
for arr in ansMap:
    for x in arr:
        if x == 1:
            ans += 1
print(ans)
