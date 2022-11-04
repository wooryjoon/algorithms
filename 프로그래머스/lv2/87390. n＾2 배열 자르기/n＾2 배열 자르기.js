function solution(n, left, right) {
  //i번째 배열의 첫번째 원소는 i 임. i가 i번 반복되고, 남은 칸에는 i+1.
    let answer = [];
    
    for (let i = left; i <= right; i++){
    answer.push(Math.max( Math.floor(i / n) + 1,  (i % n) + 1));
    }
    return answer;
}