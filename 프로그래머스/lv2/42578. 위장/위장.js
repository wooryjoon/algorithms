function solution(clothes) {
    //의상종류를 키값으로 해서 밸류에 갯수 추가

    var answer = 0;
    let hash = {};
    for (let i = 0; i < clothes.length; i++) {
        if (!hash[clothes[i][1]]) hash[clothes[i][1]] = 1;
        else hash[clothes[i][1]] ++;
    }
    answer = Object.values(hash).reduce((acc,cur) => {
         return acc * (cur+1);
    },1 );
    console.log(hash);
    return answer -1;
}