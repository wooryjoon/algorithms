n = int(input());
t = [];
for i in range(n):
    list = [*map(int,input().split())]
    t.append(list) # 입력받기 완료


def DP (N) :
    k = 2;
    for i in range(1,N):
        for j in range(0,k):
            if (j == 0):
                t[i][j] = t[i-1][j] + t[i][j]
            elif (j == i):
                t[i][j] = t[i-1][j-1] + t[i][j]
            else:
                t[i][j] =max(t[i-1][j-1] + t[i][j],t[i-1][j]+t[i][j])
        k += 1
    return max(t[N-1])

print(DP(n))
                
