function solution(numbers) {
  let prime_set = new Set();
  let arr = numbers.split("");
    
  function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i <= parseInt(Math.sqrt(n)); i++) {
      if (n % i === 0) return false;
    }
    return true;
  }
  function DFS(combination, others) {
    if (combination != "") { 
      if (isPrime(parseInt(combination))) {
        prime_set.add(parseInt(combination));
      }
    }

    for (let i = 0; i < others.length; i++) {
      let news = others.slice();
      news.splice(i, 1);
      DFS(combination + others[i], news); // numbers의 각 문자가 첫글자가 되는 case들마다 DFS 실행, 
    }
  }

  //모든 조합을 만드는 recursive
  DFS("", arr); // 인자 : 현재까지 조합된 수, 조합된 수를 제외한 나머지 후보

  return prime_set.size;
}