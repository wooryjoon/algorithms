import sys
input = sys.stdin.readline


# 문제정리
    # 문자열을 통해 만들 수 있는 모든 경우의 수를 찾고,
    # 이를 set으로 만들어 중복을 없앤다.
# 아이디어

# 시간복잡도

STR = input().rstrip()
s1 = set()
for i in range(0,len(STR)):
    for j in range(i,len(STR)):
        temp = ''.join(STR[j-i:j+1])
        s1.add(temp)
print(len(s1))