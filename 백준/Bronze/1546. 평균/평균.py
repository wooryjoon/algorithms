N = int(input())
List = list(map(int,input().split()))

# max함수로 최고점 구하고, 반복문을 통해 List의 요소를 바꿈
# 평균을 동시에 구하자.

M = max(List)
avg = 0;
sum = 0;

for i in range(N) : 
    List[i] = List[i] / M * 100
    sum += List[i]
    avg = sum / (i+1)

print(avg)