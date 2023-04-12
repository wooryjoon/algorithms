function solution(brown, yellow) {
     var answer = [];
    let i = 1;
    let j = 1;
    while (i <= 2500) {
        j = 1;
        while (j <= i) {
            if ((2 * i + 2 * j - 4) == brown && (i * j - brown) == yellow) {
                answer.push(i);
                answer.push(j);
                return answer;
            }
            j++;
        }
        i++;
    }
}