N = int(input())
List = list(map(int,input().split()))
max = List[0]
min = List[0]

for i in List :
    if i > max :
        max = i
    elif i < min :
        min = i

print(min ,max)