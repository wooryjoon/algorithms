function solution (numbers) {
    let arr = numbers.split('');
    let visited = new Array(arr.length+1).fill(false); // arr의 각 항을 방문처리할 visited 배열
    let answer  = new Set(); // answer Set에 답이되는걸 저장할거임, 근데 중복을 제외할거니까 Set객체로
    // 순열 (순서가 보장되야함)
    
        const isPrime = (number) => {
        if (number <= 1) return false; // 1이하면 소수아님
        if (number % 2 == 0 && number != 2) return false; // 2가아니면서 2로 나누어떨어지면 소수아님
        for (let i = 3; i <= Math.floor(Math.sqrt(number)); i += 2){
            if (number % i == 0) return false;
        }
        return true; // 위에서 다 안걸러졌으면 그건 소수임.
}
    const DFS = (num) => {
        if (num) { // 숫자일 때
            if (isPrime(parseInt(num)) == true) answer.add(parseInt(num));
        }
        
        //수행연산
        for (let i = 0; i < arr.length; i++){
            let add_num = arr[i];
            if (visited[i] == true) continue; // 만약에 쓴 숫자면 패스
            visited[i] = true;
            DFS(num + add_num);
            visited[i] = false; // 순서가 보장되어야함.
        }
        
    }
    
DFS('');
return answer.size;
}