import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
location = list(map(int, input().split()))

answer = 0;
#N = 10;
#K = 5;
#location = [20,3,14,6,7,8,18,10,12,15]
real_location = list(set(location)) #중복제거후 다시 배열로 변환
real_location.sort() #오름차순 정렬
real_location_len = len(real_location)
diff = [] # 각 지점간 거리차이 구해주기
for i in range(1,real_location_len):
    diff.append(real_location[i]-real_location[i-1])
diff.sort()
for i in range(0,real_location_len-K):
    answer += diff[i]

print(answer)

