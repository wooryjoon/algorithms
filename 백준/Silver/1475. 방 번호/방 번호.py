import sys
input = sys.stdin.readline

n = input().strip()
visited = [0] * 10
cnt = 0
for x in n :
    num = int(x)
    if num != 6 and num != 9:
        visited[num] += 1
    else :
        cnt += 1

if cnt % 2 == 0:
    cnt = cnt // 2
else :
    cnt = cnt // 2 + 1
    

print(max(max(visited),cnt))
