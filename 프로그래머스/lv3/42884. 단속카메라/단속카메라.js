function solution(routes) {
    const route = routes.sort((a,b)=>{
        return a[1]-b[1]
    })
    let ans = 0
    let camera = -50000
    for (let e of route) {
        const [start,end] = e
        if (camera < start) {
            camera = end
            ans ++
        }
    }
    return ans
    
    
    
}