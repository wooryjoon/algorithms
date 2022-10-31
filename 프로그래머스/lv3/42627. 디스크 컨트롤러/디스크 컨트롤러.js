function heapSort(arr) {
    for (let i = 1; i < arr.length; i++){
        let idx = i;
    while(idx > 0) {
        let parentIdx = Math.floor((idx-1)/2);
        if (arr[idx][1] < arr[parentIdx][1]){
            let temp;
            temp = arr[idx];
            arr[idx] = arr[parentIdx];
            arr[parentIdx] = temp;
            idx = parentIdx;
        }
        else break;
        }
    }
    return
}

function solution(jobs) {
    //작업이 시작되고 진행되는 시간동안 그 시간에 요청받는 작업들은 우선순위 큐에 담아줌.
    //작업이 종료 됐을때, 우선순위 큐에 있는 것중 처리시간이 가장 작은 것을 먼저 실행
    // 우선순위 큐에 아무것도 없거나, jobs 배열의 끝까지 도달할때까지 반복함.
    // jobs = [[0, 3], [1, 9], [2, 6]]
    var answer = 0;
    const priorityQueue = [];
    let i = 0;
    let time = 0;
    jobs.sort((a,b) => a[0]-b[0]) // 오름차순 정렬 (우선순위큐에 아무것도없다면, 요청순으로 작업 수행해야함)
    
    while (i < jobs.length || priorityQueue.length !== 0){
        while (i < jobs.length){
        if (jobs[i][0] <= time) { // 작업배열을 순회하며 time내에 요청받는 것들을 체크하고 우선순위큐에 넣고, 중복방지를 위해 visited를 true로 바꿔줌.
            priorityQueue.push(jobs[i]); 
            i++;
            }
        else break;
        }
        if (priorityQueue.length == 0) {
            time = jobs[i][0];
        }
        else {
            heapSort(priorityQueue);
            time += priorityQueue[0][1];
            answer += time - priorityQueue[0][0];    
            priorityQueue.shift();
        }
    
    }
    return Math.floor(answer / jobs.length);
} 