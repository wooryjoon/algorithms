function solution(board) {
    let N = board.length;
    let answer = 0;
    /*
    메모이제이션.
    현재 행에서 최대값과 그 인덱스를 구하고, 다음 행의 값들을 '값 + 이전 행 최대값'으로 바꿔준다 ()
    */
    for (let i = 0; i < board.length-1; i++) {
        let max = Math.max(...board[i])
        let index = board[i].indexOf(max);
        board[i].splice(index,1);
        let secondMax = Math.max(...board[i]);
        for (let j = 0; j < 4; j++){
            if (j === index) board[i+1][j] += secondMax;
            else board[i+1][j] += max;
        }
    }
    return Math.max(...board[N-1]);
    
    
    
}