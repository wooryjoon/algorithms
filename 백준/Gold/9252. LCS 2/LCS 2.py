import sys
input = sys.stdin.readline

# 문제 정리
    # LCS 문제, DP 활용

# 풀이 방법
    # DP테이블 설정.
    # Dp[i][j] = 1번째 문자열의 i번째 알파벳
str1 = input().strip()
str2 = input().strip()
dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)];


for i in range(1,len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1] == str2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[i][j])
ans = ""

x = len(str1)
y = len(str2)

while True :
    # 종료 조건
    if x == 0 or y == 0 : break

    # 수행 연산
    if str1[x-1] == str2[y-1] :
        ans = str1[x-1] + ans
        x -= 1
        y -= 1
    else :
        if dp[x-1][y] > dp[x][y-1] :
            x = x-1
            continue
        else :
            y -= 1
            continue
print(ans)