import sys
input = sys.stdin.readline


N,L = list(map(int,input().split())) # 새는 곳 개수, 테이프 길이
location = list(map(int,input().split())) # 새는 곳 위치
location.sort()
ans = 0
i = 0
dist = 0
while (i < N-1):
    currLoc = location[i]
    nextLoc = location[i+1]
    dist += nextLoc - currLoc
    if dist >= L : # 다음스티커는 커버 안된다 ->현재까지만 테이프 붙이기
        ans += 1 # 테이프 1개 소모
        dist = 0 
    i += 1 # 다음 테이프 확인

ans += 1 # while문이 끝나고 남은 테이프는 따로 붙이기.
print(ans)



