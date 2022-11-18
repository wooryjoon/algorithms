n = int(input());
drinks = list(map(int,input().split()))

# 5 4 3 2 1
# 0 7 


drinks.sort(reverse=True)
answer = drinks[0];
for i in range(n):
    if i == n-1:
        print(answer)
        break;
    answer += drinks[i+1] /2
    

