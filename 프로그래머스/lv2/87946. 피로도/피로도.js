/*function DFS (array, i) { // 순열 => 순서가 의미 있음
    const result = [];
    if (i === 1) return array.map( (el) => [el]);
    array.forEach ((fixed, index, origin) => {
        const rest = [...origin.slice(0,index),...origin.slice(index+1)];
        const Permutations = DFS (rest, i - 1);
        const attached = Permutations.map ((el) => [fixed, ...el]);
        result.push(...attached);
    })
    return result;
}

function solution(k, dungeons) {
// 던전을 갈 수 있는 모든 경우의 수 정렬
// 각 케이스에서 count되는 값 측정
// 그중에 제일 높은 값을 답으로 제출
    let Length = dungeons.length;
    let arr = DFS(dungeons,Length); // 던전을 도는 모든 경우의 수
    let answer = 0;
    let max = 0;
    let temp = 0;
    let j = k;
   console.log(arr);
    for (let i = 0; i < arr.length; i++){
        temp = 0;
        k = j;
        for (let j = 0; j < arr[i].length; j++){
            if (k >= arr[i][j][0]) {
                temp ++;
                k = k - arr[i][j][1];
            }
        }
        console.log(temp);
        max = Math.max(max, temp);
    }
    return max;
}*/
function solution(k, dungeons) {
    //던전을 갈 수 있는 경우의 수를 구하고, 각 경우마다 count를 판단해서 count 배열에 넣어줌.
    const countArray = [];
    const cases = [];
    function check(arr){
        let newK = k;
        let count = 0;
        for (let i = 0; i < arr.length; i++){
            if (arr[i][0] <= newK) {
                newK -= arr[i][1];
                count++;
            }
        }
        return count;
    }
    
    function DFS (result,others) {
        //종료조건
        if (result.length == dungeons.length){
            countArray.push(check(result));
        }
        //수행연산
        for (let i = 0; i < others.length; i++){
            let newPerm = result.slice();
            newPerm.push(others[i]);
            let newOthers = others.slice();
            newOthers.splice(i,1);
            DFS(newPerm,newOthers);
        }
        
    }
    DFS([],dungeons);
    return Math.max(...countArray);
}