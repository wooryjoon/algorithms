#if n < 10 ? 0을 붙여 두자리수로 만듬
# 해당 숫자의 일의자리를 십의자리로올리고, 일의자리 에는 각 자리수의 합을 넣음
# 원래 수로 돌아올때까지 반복해보자잉
N = int(input())
origin = N
count = 0
change = 0

while  True :
    if N < 10 :
        change = N * 11

    change = (N % 10) * 10 + (N//10 + N % 10) % 10
    count = count +1

    if (origin == change) : 
        print(count)
        break
    else : 
        N = change

