const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n").map(v => v.split(' ').map(Number));

const [N, M] = input.shift();
let area = input;
const cctv = [];
for (let i = 0; i < N; i++) {
  for (let j = 0; j < M; j++) {
    if (area[i][j] > 0 && area[i][j] < 6) {
      cctv.push([i, j, area[i][j]]);
    }
  }
}


const killTop = (board, x, y) => {
  for (let i = x - 1; i >= 0; i--) {
    if (board[i][y] != 6) {
      board[i][y] = '#'
    } else {
      break;
    }
  }
  return board;
}

const killBottom = (board, x, y) => {
  for (let i = x + 1; i < N; i++) {
    if (board[i][y] != 6) {
      board[i][y] = '#'
    } else {
      break;
    }
  }
  return board;
}

const killRight = (board, x, y) => {
  for (let i = y + 1; i < M; i++) {
    if (board[x][i] != 6) {
      board[x][i] = '#'
    } else {
      break;
    }
  }
  return board;
}

const killLeft = (board, x, y) => {
  for (let i = y - 1; i >= 0; i--) {
    if (board[x][i] != 6) {
      board[x][i] = '#'
    } else {
      break;
    }
  }
  return board;
}





const level1 = (newBoard, x, y, i) => {
  switch (i) {
    case 0:
      return killRight(newBoard, x, y)
    case 1:
      return killLeft(newBoard, x, y)
    case 2:
      return killTop(newBoard, x, y)
    case 3:
      return killBottom(newBoard, x, y)
  }
}

const level2 = (newBoard, x, y, i) => {
  switch (i) {
    case 0: {
      const temp = killLeft(newBoard, x, y)
      return killRight(temp, x, y)
    }
    case 1: {
      const temp = killTop(newBoard, x, y)
      return killBottom(temp, x, y)
    }
  }
}

const level3 = (newBoard, x, y, i) => {
  switch (i) {
    case 0: {
      const temp = killLeft(newBoard, x, y)
      return killBottom(temp, x, y)
    }
    case 1: {
      const temp = killLeft(newBoard, x, y)
      return killTop(temp, x, y)
    }
    case 2: {
      const temp = killRight(newBoard, x, y)
      return killBottom(temp, x, y)
    }
    case 3: {
      const temp = killRight(newBoard, x, y)
      return killTop(temp, x, y)
    }
  }
}

const level4 = (newBoard, x, y, i) => {
  switch (i) {
    case 0: {
      const temp = killLeft(newBoard, x, y)
      const temp2 = killRight(temp, x, y)
      return killBottom(temp2, x, y)
    }
    case 1: {
      const temp = killLeft(newBoard, x, y)
      const temp2 = killRight(temp, x, y)
      return killTop(temp2, x, y)
    }
    case 2: {
      const temp = killTop(newBoard, x, y)
      const temp2 = killBottom(temp, x, y)
      return killLeft(temp2, x, y)
    }
    case 3: {
      const temp = killTop(newBoard, x, y)
      const temp2 = killBottom(temp, x, y)
      return killRight(temp2, x, y)
    }
  }

}

const level5 = (newBoard, x, y) => {
  const temp = killTop(newBoard, x, y)
  const temp2 = killBottom(temp, x, y)
  const temp3 = killRight(temp2, x, y)
  const temp4 = killLeft(temp3, x, y)
  return temp4
}

const check = (board) => {
  let res = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (board[i][j] == 0) {
        res++;
      }
    }
  }
  return res;
}



let answer = Infinity;
const solve = (board, cnt) => {
  if (cnt == cctv.length) {
    const temp = check(board);
    if (temp < answer) {
      // console.log(temp)
      // console.log(board.map(v => v.join(' ')).join('\n'))
      answer = temp
    }
    return;
  } else {
    const [x, y, c] = cctv[cnt]
    switch (c) {
      case 1:
        for (let i = 0; i < 4; i++) {
          const newBoard = [];
          board.map(v => newBoard.push([...v]));
          solve(level1(newBoard, x, y, i), cnt + 1);
        }
        break;
      case 2:
        for (let i = 0; i < 2; i++) {
          const newBoard = [];
          board.map(v => newBoard.push([...v]));
          solve(level2(newBoard, x, y, i), cnt + 1);
        }
        break;
      case 3:
        for (let i = 0; i < 4; i++) {
          const newBoard = [];
          board.map(v => newBoard.push([...v]));
          solve(level3(newBoard, x, y, i), cnt + 1);
        }
        break;
      case 4:
        for (let i = 0; i < 4; i++) {
          const newBoard = [];
          board.map(v => newBoard.push([...v]));
          solve(level4(newBoard, x, y, i), cnt + 1);
        }
        break;
      case 5:
        const newBoard = [];
        board.map(v => newBoard.push([...v]));
        solve(level5(newBoard, x, y), cnt + 1);
        break;
    }
  }
}

solve(area, 0)
console.log(answer)