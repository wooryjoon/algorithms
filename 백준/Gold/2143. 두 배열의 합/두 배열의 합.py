import sys
input = sys.stdin.readline
from bisect import bisect_left,bisect_right
# A,B에서 나올 수 있는 부분합 모두 구하기
# 오름차순 정렬
T = int(input())
n = int(input())
A = list(map(int,input().split()))
m = int(input())
B = list(map(int,input().split()))
ans = 0
sumA = []
sumB = []
for i in range(n):
    temp = 0
    for j in range(i,n):
        temp += A[j]
        sumA.append(temp)
for i in range(m):
    temp = 0
    for j in range(i,m):
        temp += B[j]
        sumB.append(temp)
sumA.sort()
sumB.sort()

i = 0
while i < len(sumA) :
    a = sumA[i]
    b = T-a
    
    a_length = bisect_right(sumA,a) - bisect_left(sumA,a)
    b_length = bisect_right(sumB,b) - bisect_left(sumB,b)
    ans += a_length * b_length
    i += a_length
print (ans)