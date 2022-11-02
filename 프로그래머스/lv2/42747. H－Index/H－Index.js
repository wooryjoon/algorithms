/*function solution(citations) {
    let n = citations.length;
    let h;
    //오름차순 정렬
    citations.sort((a,b)=>b-a);
    
    for (let i = 0; i < citations.length; i++){
        let element = citations[i];
        if (element <= i+1) {
            h = i+1;
            break;
        }
    }
 return h;
}*/
function solution(citations) {

    citations.sort((a, b) => b - a);

    let answers = 0;
    for (let i = 0; i < citations.length; i++) {
        if (i < citations[i]) {
            answers++;
        }
    }

    return answers;
}

console.log(solution([47, 42, 32, 28, 24, 22, 17, 15, 10, 10, 8]));
console.log(solution([3, 0, 6, 1, 5]));