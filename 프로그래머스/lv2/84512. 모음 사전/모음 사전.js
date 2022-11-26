function solution(word) {
    // 순서대로 사전을 만들면 문제 끝.
    let arr = ['A','E','I','O','U'];
    let dict = [false];
    const DFS = (alpha) => { // 각 단계마다 dict에 푸쉬.
        dict.push(alpha);
        if (alpha.length == 5) return;
        for (let i = 0; i < arr.length; i++){
            let sum_alpha;
            sum_alpha = alpha + arr[i]; 
            DFS (sum_alpha);
        }
        
    }
    arr.forEach(alpha => {
        DFS(alpha);
    })
    return dict.indexOf(word);
}