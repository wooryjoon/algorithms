
def hanoi (n,start,end) : # 하노이
    # 종료조건
    if (n == 1):
        print(start,end)
        return 
    #수행 연산
    hanoi(n-1,start,6-start-end) # n-1개의원반을 가운데로 옮김
    print(start,end) # 남은 한개의 원반을 끝으로 옮김
    hanoi(n-1,6-start-end,end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)