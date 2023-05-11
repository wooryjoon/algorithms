function solution(routes) {
    const route = routes.sort((a,b)=>{
        return b[0]-a[0]
    })
    // stack을 돌면서 endPoint는 둘중에 작은 쪽으로 유지됨.
    ans = 1
    stack = []
    endPoint = -1000
    while (route.length) {
        if (!stack.length) {
            stack.push(route.pop())
            endPoint = stack.at(-1)[1]
            continue
        }
        
        [nextStart,nextEnd] = route.at(-1)
        
        if (nextStart <= endPoint) {
            route.pop()
            endPoint = Math.min(endPoint,nextEnd)
            continue
        }
        ans ++
        stack.push(route.pop())
        endPoint = stack.at(-1)[1]
    }
    return ans
}