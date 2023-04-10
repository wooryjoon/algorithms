import sys
input = sys.stdin.readline

# 3*3칸을 돌면서, 정답과 비교해서 바꿔야할게 더 많으면 바꾼다.
# 예외 사항은 나중에 처리

def sol() :
    n,m = list(map(int,input().split()))
    arr = [list(input().strip()) for _ in range(n)]
    answer = [list(input().strip()) for _ in range(n)]
    ans = 0
    if (n<3 or m<3) and (arr==answer):
        return 0
    if (n<3 or m<3) and (arr!=answer):
        return -1

    def modify (x,y) :
        for i in range(x,x+3):
            for j in range(y,y+3):
                arr[i][j] = '0' if arr[i][j] =='1' else '1'
            
    def check() :
        for i in range(n):
            for j in range(m):
                if arr[i][j] != answer[i][j]:
                    return False
        return True

    for i in range(n-2):
        for j in range(m-2):
            if arr[i][j] != answer[i][j] : # 바꿔야한다면
                modify(i,j)
                ans += 1
            if check():
                return ans
    return -1

print(sol())