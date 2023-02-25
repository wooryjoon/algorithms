import heapq

def solution(jobs):
    n_jobs = len(jobs)
    h = []
    result, current_time, i = 0, 0, 0
    # 이전 작업의 시작시간
    start = -1

    while i < n_jobs :
        for job in jobs:
            # 수행할 수 있는 작업의 판별조건
            # 요청 시간이 이전작업의 시작시간 보다 크고, 현재 시간보다 작거나 같은 작업을 최소 힙에 삽입
            if start < job[0] <= current_time:
                # 처리 시간이 작은 작업이 우선적으로 처리되어야 함
                heapq.heappush(h, [job[1], job[0]])
        if len(h) > 0:
            et, st = heapq.heappop(h)
            # 시작 시간을 현재 시간으로 갱신
            start = current_time
            # 현재 시간에 작업 소요 시간을 더해 현재 시간 갱신
            current_time += et
            #대기 시간 및 처리시간 누적
            result += (current_time - st)
            i += 1
        else:
            # 힙이 비어있는 상태라면 작업을 받기 위해 현재 시간 1증가
            current_time += 1
    return int(result/n_jobs)