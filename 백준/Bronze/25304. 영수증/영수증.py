myCost = int(input())
N = int(input())
sum = 0;
for i in range(0,N) :
    price,count = map(int,input().split())
    sum += price*count

if myCost == sum :
    print('Yes')
else :
    print('No')    
