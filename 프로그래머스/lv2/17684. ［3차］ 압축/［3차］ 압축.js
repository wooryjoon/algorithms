function solution(msg) {
    let dict =['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T'
              ,'U','V','W','X','Y','Z']; // 사전 준비
    let i = 0;
    let answer = [];
    while (msg[i]){
        let target = '';
        let curr_i = i;
        let new_word = '';
        for (let j = i; j < msg.length; j++){
            if (dict.includes(target + msg[j])) { // target에 하나씩 더한 값이 사전에 존재하면 target을 최신화
                target = target + msg[j];
                curr_i ++; // 다음 순회 때 인덱스 움직일 크기
            }
            else break;
        }
      
        answer.push(dict.indexOf(target)); // 출력번호를 정답배열에 넣음
        if (curr_i >= msg.length) break; // 모든문자열을 탐색하면 반복문 종료
        new_word = target + msg[curr_i]; // 사전에 넣을 새로운 문자열을 만듬. (원래target+그다음인덱스)
        dict.push(new_word); // 사전에 새 문자열 넣음, (출력번호는 index값이 됨)
        i = curr_i;
    }
    return answer;
}