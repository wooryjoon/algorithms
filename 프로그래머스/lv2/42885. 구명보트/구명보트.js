function solution(people, limit) {
    // 두개의 합이 limit을 넘지 않는 선에서 가장 큰 짝을 맞춤.
    // 해당 인덱스가 limit보다 크면 count++ 하고 i++
    // limit보다 작으면, 그 이후의 인덱스를 탐색하며 두개의 합이 100이하면서 가장 큰 경우를 탐색(내림차순정렬)
    let count = 0;
    let arr = people.sort((a,b) => a - b);
    
    while (arr.length != 0) {
        let first = arr[0];
        let last = arr[arr.length-1];
        
        if (first + last <= limit) { // 타겟이 되는 조건을 if문에 넣기
            arr.shift();
            arr.pop();
            count++;
        } else {
            arr.pop();
            count++;
        }
    }
   return count;
}
