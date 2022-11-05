function solution(d, budget) {
    //배열을 오름차순으로 소팅하고, 예산에서  각 인덱스의 요소를 빼준다. 버젯 - 요소 값이 0 이하가 되면 종료. 카운트 반환
    let d_asc = d.sort((a,b) => a-b);
    let count = 0;
    while (budget >= 0){
        budget -= d_asc[count];
        count++;
    }
    return count-1 ;
}