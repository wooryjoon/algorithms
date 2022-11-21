import sys

input = sys.stdin.readline
N = int(input()) # 크레인 갯수
limitWeight = list(map(int, input().split())) # 각 크레인의 무게제한
M = int(input()) # 박스 갯수
boxWeight = list(map(int, input().split())) # 박스의 무게

# 무거운 박스를 리밋웨잇이 큰놈이 들수록 좋다?
# 박스웨이트를 내림차순 정렬, 리밋웨이트도 내림차순 정렬
# 박스웨이트 배열순회하면서 덱스첫항부터 순서대로 각각 매칭,

"""N = 4
limitWeight = [23,32,25,28]
M = 10
boxWeight = [5,27,10,16,24,20,2,32,18,7]
"""
limitWeight.sort(reverse=True)
boxWeight.sort(reverse=True)
i = 0;
j = 0;
time = 0;
# 에외처리 여기에 나중에 할 것
if (limitWeight[0] < boxWeight[0]) :
    print(-1)  
else :
    while sum(boxWeight) != 0: # boxweight배열의 모든요소가 0이될때까지 반복
        j = 0;
        i = 0;
        while (True): # 박스의끝에 도달하거나, 크레인끝에도달할때까지
            try :
                if boxWeight[i] == 0 :
                    i = i+1 # -1이라는건 옮겼단 뜻이니까 다음칸으로 이동하고 패스
                    continue;
                if limitWeight[j] >= boxWeight[i]:
                    boxWeight[i] = 0; # 옮긴거는 -1로바꿔줌
                    i = i+1 
                    j= j+1
                else:
                    i = i+1
            except:
                break;
        time = time + 1

    print(time)    
            
        
        