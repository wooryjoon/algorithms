import sys
input = sys.stdin.readline

#문제 정리
    # A 빌딩에서 B빌딩이 보이려면 각 빌딩의 꼭대기를 잇는 선분 사이에
    # 다른 빌딩의 꼭대기가 접하거나 걸리지 않아야 한다.

# 찾고자 하는 값 
    # 가장 많은 고층 빌딩을 볼 수 있는 빌딩을 찾고,
    # 그 빌딩에서 볼 수 있는 "빌딩의 개수" 출력

# 아이디어
    # 단순히 빌딩의 크기만 비교해서는  정확히 알 수 없다.
    # 빌딩 사이의 기울기의 절대값의 크기를 바탕으로 비교한다.
    # 기울기 = (y증가량 // x증가량)

# 풀이 과정
    # 모든 빌딩을 돌며 각 빌딩에서 볼 수 있는 빌딩들을 조건에 맞는 식을 통해 
    # 완전 탐색 한다.

def sol() :
    n = int(input())
    heights = list(map(int,input().split()))
    ans = -10
    def extractGug(x1,x2,y1,y2) : # 기울기 구하는 함수
        return (y2-y1) / (x2-x1)
    
    def findLeft(i,count) : 
        # 현재 빌딩과의 기울기가 지금까지의 min기울기 값보다 작다면 ,
        # 그 빌딩은 볼 수 있다. 
        if i == 0 : return 0
        minGug = None
        for j in range(i-1,-1,-1):
            currGug = extractGug(i,j,heights[i],heights[j])
            if minGug == None or currGug < minGug :
                minGug = currGug
                count += 1
        return count
    def findRight(i,count) :
        # 현재 빌딩과의 기울기가 지금까지의 max기울기 값보다 크다면,
        # 그 빌딩은 볼 수 있다.
        if i == n-1 : return 0
        maxGug = None
        for j in range(i+1,n):
            currGug = extractGug(i,j,heights[i],heights[j])
            if maxGug == None or currGug > maxGug:
                count += 1
                maxGug = currGug
        return count
    for i in range(n):
        count = 0
        count = findLeft(i,0) + findRight(i,0)
        ans = max(ans,count)
    return ans
print(sol())