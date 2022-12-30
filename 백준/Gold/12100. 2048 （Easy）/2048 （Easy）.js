const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let N = input.splice(0, 1).join("");
let board = [];

N = Number(N);
for (let str of input) {
  board.push(str.split(" ").map(Number));
}
// 좌측 이동시 수행할 함수
const left = (board) => {
  let newBoard = [];
  for (let row of board) {
    let arr = [];
    let isUnion = Array(N).fill(false);
    for (let e of row) {
      if (e === 0) continue;
      if (arr.length === 0) {
        arr.push(e);
        continue;
      }
      let last = arr.length - 1;
      if (arr[last] === e && isUnion[last] === false) {
        arr[last] += arr[last];
        isUnion[last] = true;
      } else if (arr[last] != e || isUnion[last] == true) {
        arr.push(e);
      }
    }
    for (let i = arr.length; i < N; i++) {
      arr.push(0);
    }
    newBoard.push(arr);
  }
  return newBoard;
};
//우측 이동시 수행할 함수
const right = (board) => {
  let newBoard = [];
  for (let row of board) {
    let arr = [];
    let isUnion = Array(N).fill(false);
    for (let i = row.length - 1; i >= 0; i--) {
      if (row[i] === 0) continue;
      if (arr.length === 0) {
        arr.push(row[i]);
        continue;
      }
      let last = arr.length - 1;
      if (arr[last] === row[i] && isUnion[last] === false) {
        arr[last] += arr[last];
        isUnion[last] = true;
      } else if (arr[last] != row[i] || isUnion[last] == true) {
        arr.push(row[i]);
      }
    }
    for (let i = arr.length; i < N; i++) {
      arr.push(0);
    }
    newBoard.push(arr.reverse());
  }
  return newBoard;
};
// 아래쪽 이동시 수행할 함수
const down = (board) => {
  let newBoard = Array.from(Array(N), () => Array(N).fill(false));
  for (let y = 0; y < N; y++) {
    let arr = [];
    let isUnion = Array(N).fill(false);
    for (let x = N - 1; x >= 0; x--) {
      if (board[x][y] == 0) continue;
      if (arr.length == 0) {
        arr.push(board[x][y]);
        continue;
      }
      let last = arr.length - 1;
      if (arr[last] === board[x][y] && isUnion[last] === false) {
        arr[last] += arr[last];
        isUnion[last] = true;
      } else if (arr[last] != board[x][y] || isUnion[last] == true) {
        arr.push(board[x][y]);
      }
    }
    for (let i = arr.length; i < N; i++) {
      arr.push(0);
    }
    arr = arr.reverse();
    for (let x = 0; x < N; x++) {
      newBoard[x][y] = arr[x];
    }
  }
  return newBoard;
};
// 위쪽 이동시 수행할 함수
const up = (board) => {
  let newBoard = Array.from(Array(N), () => Array(N).fill(false));
  for (let y = 0; y < N; y++) {
    let arr = [];
    let isUnion = Array(N).fill(false);
    for (let x = 0; x < N; x++) {
      if (board[x][y] == 0) continue;
      if (arr.length == 0) {
        arr.push(board[x][y]);
        continue;
      }
      let last = arr.length - 1;
      if (arr[last] === board[x][y] && isUnion[last] === false) {
        arr[last] += arr[last];
        isUnion[last] = true;
      } else if (arr[last] != board[x][y] || isUnion[last] == true) {
        arr.push(board[x][y]);
      }
    }
    for (let i = arr.length; i < N; i++) {
      arr.push(0);
    }
    for (let x = 0; x < N; x++) {
      newBoard[x][y] = arr[x];
    }
  }
  return newBoard;
};
const deepCopy = (board) => {
  let copy = [];
  for (let arr of board) {
    let temp = [];
    for (let e of arr) {
      temp.push(e);
    }
    copy.push(temp);
  }
  return copy;
};
const findMax = (board) => {
  let ans = 0;
  for (let arr of board) {
    let max = Math.max(...arr);
    ans = Math.max(ans, max);
  }
  return ans;
};
let max = 0;
// DFS 돌려서 각 함수들을 수행하는 케이스 연산
// depth가 5가 됐을 때 해당 board에서 가장 큰 값을 계속 갱신

const DFS = (board, depth) => {
  //종료조건
  if (depth === 5) {
    max = Math.max(max, findMax(board));
    return;
  }
  //수행연산
  /*
  4방향 연산 모두 DFS 돌리기.
  */
  let newArr = deepCopy(board);
  DFS(left(newArr), depth + 1);

  newArr = deepCopy(board);
  DFS(right(newArr), depth + 1);

  newArr = deepCopy(board);
  DFS(down(newArr), depth + 1);

  newArr = deepCopy(board);
  DFS(up(newArr), depth + 1);
};
DFS(board, 0);
console.log(max);
