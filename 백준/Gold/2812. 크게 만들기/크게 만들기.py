import sys
input = sys.stdin.readline

# 아이디어
    # num의 첫번쨰 원소부터 stack에 값을 넣는다.
    # 만약 count가 k보다 작다면,
        # next가 top보다 크면, pop하는 연산을 반복 수행한다. 그때마다 count ++
    # count == k : 무지성 append()
# 변수 사용

n,k = list(map(int,input().split()))
arr = list(input().strip())
num = [int(e) for e in arr ]
stack = []
cnt = 0
for curr in num :
    if not stack : 
        stack.append(curr)
        continue

    if cnt == k :
        stack.append(curr)
        continue

    if curr > stack[-1] :
        while stack and stack[-1] < curr and cnt < k :
            stack.pop()
            cnt += 1

    stack.append(curr)

while (cnt < k) :
    cnt += 1
    stack.pop()
    
print(''.join(map(str,stack)))