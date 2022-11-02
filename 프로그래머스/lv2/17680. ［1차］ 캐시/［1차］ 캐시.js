function solution(cacheSize, cities) {
    var answer = 0;
    //순서대로 cache에 넣는데 최대 cacheSize만큼만 넣을 수 있고, 초과해서받게되면 맨앞꺼 배고 추가함.
    //cities 배열을 순회하며 각 요소가 cache에 있는지 확인
    // if (있다) answer += 1; 캐시에 넣음
    // 없다 answer += 5; 캐시에 넣음
    //도시는 대소문자 구분 안한다. (애초에 전부 소문자로 만들어버리자)
    const cache = [];
    let Ncities = cities.map((string) =>{
        let Nstr = string.toLowerCase();
        return Nstr;
        })
    console.log(Ncities);
    function LRU(str){
        if(cacheSize == 0) return;
        
        if(cache.includes(str)){
            cache.splice(cache.indexOf(str),1);
            cache.push(str);
        }
        else {
            if (cache.length == cacheSize) cache.shift();
            cache.push(str);
        }
    }
    
    for (let i = 0; i < cities.length; i++){
        if (cache.includes(Ncities[i])) {
            answer += 1;
        }
        else{
            answer += 5;
        }
        LRU(Ncities[i],i);
    }
    return answer;
}