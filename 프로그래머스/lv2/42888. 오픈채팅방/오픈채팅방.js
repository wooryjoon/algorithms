function solution(record) {
    //record를 공백기준split 했을때
    // 첫번째 항은 Enter Leave Change
    //두번째 항은 유저아이디
    // 세번째 항은 닉네임
    // 각각의 최종 닉네임을 먼저 결정.
    // 배열을 순회하면서, uid를 key로하고 닉네임을 value로 하는 객체를 생성.
    let id_nickname = {}; // key : 유저아이디, value : 닉네임
    let arr = [];
    let answer = [];
    for (let i = 0; i <record.length; i++){
        arr.push(record[i].split(' '))
    };
    for (let i = 0;i < arr.length; i++){
        let uid = arr[i][1];
        let nickname = arr[i][2];
        if (nickname){
        id_nickname[uid] = nickname;
        }
    }
    for (let i = 0;i < arr.length; i++){
        //`string text ${expression} string text`
        let action = arr[i][0];
        let uid = arr[i][1];
        let nickname = arr[i][2];
        if (action =='Enter'){
            answer.push(`${id_nickname[uid]}님이 들어왔습니다.`);
        }
        else if (action =='Leave') {
            answer.push(`${id_nickname[uid]}님이 나갔습니다.`);
        }
    }
    return answer;
}