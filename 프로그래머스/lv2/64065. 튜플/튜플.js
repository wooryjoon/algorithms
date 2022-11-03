function solution(s) {
    var answer = [];
    let parse = [];
    let temp = [];
    let str = '';
    // 대괄호 사이에 항이 1개인건 무조건 첫번째 자리수.
    // 두개짜리중 첫번째 자리수가 아닌게 두번째자리수.
    /// 
    // 자리수 확정될때마다 중복방지 위해서 visited 에 담아주기?
    //주어진 문자열을 어떻게 파싱할까.. => 문자열을 순회하면서 숫자가 나오고부터 숫자가 안나오기 전까지 나온 숫자를 
    for (let i = 1; i < s.length - 1; i++){
        if (s[i] == '{' ) {
            temp = [];
        }
        
        if (s[i] >= '0' && s[i] <= '9') {
            str += s[i];
           if(s[i + 1] == ',' || s[i+1] == '}') {
               temp.push(parseInt(str));
               str = '';
            }
        }
        else if (s[i] == '}') parse.push(temp);
    }
    
    for (let i = 1; i <= parse.length; i++){
        for (let j = 0; j < parse.length; j++){
            if (parse[j].length === i){
                let newparse = parse[j].filter((elem) => {
                    return !answer.includes(elem);
                })
                answer.push(newparse[0]);
            }
        }
    }
    return answer;
}