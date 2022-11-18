n = int(input());
roads = list(map(int,input().split()))
costs = list(map(int,input().split()))

# 주유소 가격, 거리 배열을 한번에 움직이면서 비교, 현재 주유소가격이 이전 도시의 가격보다 싸다면?
# 다음 도시로 갈때는 현재도시의 주유소 가격을 쓴다
# 아니라면? 이전 도시의 주유소 가격을 그대로 쓴다.
res = 0;
m = costs[0];

for i in range(n-1):
    if costs[i] < m:
        m = costs[i];
    res += m * roads[i]
print(res) 
    