n = int(input())
arr = list(map(int,input().split()))
arr.sort()
maxy = -1;
if n % 2 == 0:
    for i in range(n//2):
        sum = arr[i]+arr[n-1-i];
        maxy = max(sum,maxy)
    answer = maxy;
else:
    tail = arr[n-1]
    for i in range((n-1)//2):
        sum = arr[i]+arr[n-2-i]
        maxy = max(sum,maxy)
    answer = max(tail,maxy)

print(answer)

