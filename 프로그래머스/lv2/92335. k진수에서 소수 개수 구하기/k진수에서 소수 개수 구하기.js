const sosu  = (string) => {
    let number = parseInt(string);
    if (number == 1) return false;
    if (number == 2) return true;
    if (number % 2 == 0) return false;
    for (let i = 3; i <= Math.floor(Math.sqrt(number)); i += 2){
        if (number % i === 0) return false;
    }
    return true;
}
function solution(n, k) {
    // n 을 k진수로 바꾼다.
    // 바꾼 수를 0을 기준으로 split한다
    let str = '';
    let count = 0;
    while (n > 0) {
        str = n % k + str;
        n = Math.floor(n / k);
    }
    
    let arr = str.split('0');
    
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == '') continue;
        if (sosu(arr[i])) count++;
    }
    return count;
}