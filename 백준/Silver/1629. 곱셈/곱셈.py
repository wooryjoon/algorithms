[A,B,C] = list(map(int,input().split()))


def POW (A,B,C) : # A의 B승을 C로 나눈 나머지
    #종료조건
    if (B == 1): return A % C
    #수행연산  
    val = POW(A,B//2,C)
    val = (val * val) % C
    if (B % 2 == 0): return val # 짝수인 경우
    else: 
        return (val * A) % C

print(POW(A,B,C))