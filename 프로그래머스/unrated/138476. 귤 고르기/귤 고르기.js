function solution(k, tangerine) {
    // set으로 귤 종류 카운팅
    // tangerine에 들어있는 것들 종류별로 몇개인지 구분하고, 종류가 많은것부터 담기.
    let 종류 = {};
    let 종류정렬 = [];
    
    for (let v of tangerine){
        if (!종류[v]) 종류[v] = 1;
        else 종류 [v] ++;
    }
    
    for (let v in 종류){
        종류정렬.push(종류[v])
    }
    종류정렬.sort((a,b)=> b-a)
    
    for (let i = 0; i < 종류정렬.length; i++){
        k = k - 종류정렬[i];
        if (k <= 0) return i+1;
    }
}