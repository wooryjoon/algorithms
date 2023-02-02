import sys
import heapq

t = int(sys.stdin.readline())

# 테스트 케이스만큼 반복한다.
for _ in range(t):
    k = int(sys.stdin.readline())
    heap_max = []
    heap_min = []
    visited = [False] * k # 정수 여부

    # 반복문을 통행 연산을 수행한다.
    for i in range(k):
        a, b = map(str, sys.stdin.readline().split())

        # 삽입 연산
        if a == "I":
            heapq.heappush(heap_max, (-int(b), i)) # 최대 힙
            heapq.heappush(heap_min, (int(b), i)) # 최소 힙
            visited[i] = True # 정수 생성

        # 제거 연산
        else:
            # 최대 힙 제거
            if b == "1":
                # 반복문을 통해 이미 제거 된 정수는 팝하여 제거
                while heap_max and visited[heap_max[0][1]] == False:
                    heapq.heappop(heap_max)

                # 최대 힙이 있으면 최대 힙 제거
                if heap_max:
                    visited[heap_max[0][1]] = False
                    heapq.heappop(heap_max)

            # 최소 힙 제거
            else:
                # 반복문을 통해 이미 제거된 정수는 팝하여 제거
                while heap_min and visited[heap_min[0][1]] == False:
                    heapq.heappop(heap_min)

                # 최소 힙이 있으면 최소 힙 제거
                if heap_min:
                    visited[heap_min[0][1]] = False
                    heapq.heappop(heap_min)

    # 정수가 없다면 "EMPTY" 출력
    if True not in visited:
        print("EMPTY")
    else:
        # 정수가 있다면
        # 연산이 끝난 후 제거 되지 못한 최대 힙과 최소 힙을 팝하여 제거
        while heap_max and visited[heap_max[0][1]] == False:
            heapq.heappop(heap_max)
        while heap_min and visited[heap_min[0][1]] == False:
            heapq.heappop(heap_min)

        # 최대 힙, 최소 힙 출력
        print(-heap_max[0][0], heap_min[0][0])