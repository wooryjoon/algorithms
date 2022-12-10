function solution(skill, skill_trees) {
    // skill_trees 문자열을 순회하면서, skill배열에 있는 문자면 따로 빼서 배열에 담는다.
    // 이를 반복한 후에, 새로 생성된 배열을 순회하면서 각 문자가 skill배열에서의 index위치를 체크하고,
    // 이 배열이 0,1,2 순으로 잘 배열됐는지 확인해서 알맞으면 return true;
    let skill_array = [];
    let answer = 0;
    const isRightOrder = (arr,length) => {
        let compare = Array(length).fill(-1).map((e,i) => i);
        for (let i = 0; i < length; i++){
            if (arr[i] !== compare[i]) return false;
        }
        return true;
    }
    for (let arr of skill_trees) {
        let temp = [];
        for (let str of arr){
            if (skill.includes(str)){
                let strIndex = skill.indexOf(str);
                temp.push(strIndex);
            }
        }
        skill_array.push(temp);
    }
    for(let e of skill_array){
        isRightOrder(e,e.length) ? answer += 1 : answer = answer 
    }
    return answer;
}