import sys
input = sys.stdin.readline
from bisect import bisect_left ,bisect_right
from collections import deque

# 문제정리
    # 덧셈은 괄호를 어디다 치든간에 똑같은거 아닌가?
    # 문자열 탐색하면서 -가 최초로 등장하면 괄호치고, 이후 -가 나오기 전까지
    # 괄호로 묶어준다.
    # 반복.
# 아이디어
    # 
# 시간복잡도

str = input().rstrip().split('-') 
ans = 0

for x in str[0].split('+'):
    ans += int(x)

for x in str[1:]:
    for y in x.split('+'):
            ans -= int(y)

print(ans)

