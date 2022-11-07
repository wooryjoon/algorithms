function solution(number, k) {
    //스택에 첫 항을 넣는다.
    //스택에 들어있는 마지막 값보다 배열의 값이 크면, 스택에 있는거 pop, 
    
    let arr = number.split('').map((a) => parseInt(a));
    let stack = [];
    
    for (let i = 0; i < arr.length; i++){
     let element = arr[i];
        while (k > 0 && stack[stack.length - 1] < element) {
            stack.pop();
            k = k - 1;
        }
        stack.push(arr[i]);
    }
    stack.splice(stack.length-k,k);
    return stack.join('');
}