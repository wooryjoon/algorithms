function rightCheck (str){
    let count1 = 0; // ()
    let count2 = 0; // {}
    let count3 = 0; // []
    
    for (let i = 0; i < str.length; i++){
        if (count1 <0 || count2 <0 || count3 <0) return false;
        
        if (str[i] == '('){
            count1++;
            if (str[i+1] == '}' || str[i+1] == ']') return false;
        }
        else if (str[i] == '{'){
            count2++;
            if (str[i+1] == ')' || str[i+1] == ']') return false;
        }
        else if (str[i] == '['){
            count3++;
            if (str[i+1] == '}' || str[i+1] == ')') return false;
        }
        else if (str[i] == ')') count1--;
        else if (str[i] == '}') count2--;
        else if (str[i] == ']') count3--;
    }
    if (count1 == 0 && count2 == 0 && count3 ==0) return true;
    else return false;
}    
function solution(s) {
    const S = s.split('');
    let x = 0;
    //왼쪽으로 돌리는 함수.
    //해당 문자열이 올바른 괄호인지 판단하는 함수
    
    for (let i = 0; i < S.length; i++) {
        if (i >= 1){
        let piece = S.shift();
        S.push(piece);
        }
        if (rightCheck(S)) x++;
    }
    return x;
}