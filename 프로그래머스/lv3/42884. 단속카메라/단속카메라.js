function solution(routes) {
    let camera = [];
    routes.sort((a,b) => {
        return a[1]-b[1];
    }); // 루트 배열을 출구점 기준으로 오름차순 정렬
    camera.push(routes[0][1]);
    for (let i = 1; i < routes.length; i++){
        let [from,to] = routes[i];
        if (from <= camera[camera.length-1]) continue;
        camera.push(to);
    }
    return camera.length;
}