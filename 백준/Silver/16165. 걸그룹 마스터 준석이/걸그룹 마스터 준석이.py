import sys
input = sys.stdin.readline


# 문제정리
    # 퀴즈 종류가 0일 경우 팀 멤버 전원 한줄씩 출력
    # 퀴즈 종류가 1일 경우 팀 이름 출력
# 아이디어

# 시간복잡도

n,m = list(map(int,input().split())) # 걸그룹 수, 문제 수
dict = {}
for _ in range(n) :
    name = input().rstrip()
    memberLength = int(input())
    temp = [input().rstrip() for _ in range(memberLength)]
    temp.sort()
    dict[name] = temp
for _ in range(m) :
    prblms = input().rstrip()
    type = input().rstrip()
    if type == '0' : # 멤버 전원 출력
        ans = '\n'.join(dict[prblms])
        print(ans)
    if type == '1': # 팀 이름 출력
        for k in dict.keys() :
            if prblms in dict[k]:
                print(k)
                break


