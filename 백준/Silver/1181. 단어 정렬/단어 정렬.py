import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N) :
    str = input().strip()
    arr.append(str)
arr = list(set(arr))
arr.sort(key=lambda x:(len(x),x))

print('\n'.join(arr))
