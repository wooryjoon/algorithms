from collections import deque,defaultdict

def solution(gems):
    # 총 몇개 종류인지 확인
    # start,end 설정
    # gems를 돌면서 deque에 하나씩 담고 길이 check해서 정답 출력 유무
    # 가장 최근에 담은 gem이 deque의 0번째랑 같으면 start ++
    answer = []
    setOriginGems = set(gems)
    setOriginGemsLength = len(setOriginGems)
    dequeGems = deque()
    setGems = defaultdict(int)
    start,end = 1,0
    
    for i in range(len(gems)) :
        end += 1
        currGem = gems[i]
        dequeGems.append(currGem)
        setGems[currGem] += 1
        if len(dequeGems) >= 2 and dequeGems[0] == dequeGems[-1] :
            dequeGems.popleft()
            setGems[currGem] -= 1
            start += 1
        if len(setGems) == setOriginGemsLength :
            while True :
                if setGems[dequeGems[0]] > 1:
                    start += 1
                    setGems[dequeGems[0]] -= 1
                    dequeGems.popleft()
                else: break
            answer.append((start,end))
    answer.sort(key = lambda x : (x[1]-x[0],x[0]))
    return answer[0]