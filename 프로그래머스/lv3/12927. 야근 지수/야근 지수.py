from heapq import heappush, heappop
def solution(n, works):
    # 야근피로도 = 야근 시작 시점에 남아있는 일의 작업량의 제곱을 합한 값
    # 이를 최소화.
    # 1시간동안 1만큼 처리 가능
    # n만큼 1을 뺄 수 있는 기회가 있고, 이를 적절히 빼서 제곱합을 최소로.
    # works가 거의 다 비슷하게 빼주는게 좋다?
    # 각 시점에서 works의 최대값을 빼준다.
    # n번만큼 반복문 돌면서, 최대힙pop후 -1 후 다시 push
    answer = 0
    pq = []
    if sum(works) <= n : return 0
    for e in works:
        heappush(pq,-e)
    for i in range(n):
        temp = -heappop(pq) - 1
        heappush(pq,-temp)
    for e in pq :
        answer += e ** 2
    return answer