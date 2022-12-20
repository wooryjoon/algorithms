let N = require("fs").readFileSync("/dev/stdin").toString().trim();
N = Number(N);
// 이차원 map만들고 전부다 공백으로 채워놓는다.
let map = Array.from(Array(N), () => Array(2 * N - 1).fill(" "));

const printStar = (N, i, j) => {
  // 그려야할 지도 사이즈, 기준 좌표 i,j
  if (N == 3) {
    map[i][j + 2] = "*";
    map[i + 1][j + 1] = "*";
    map[i + 1][j + 3] = "*";
    for (let k = 0; k <= 4; k++) {
      map[i + 2][j + k] = "*";
    }
    return;
  } else {
    // 좌표에 넣는 x,y는 각 기준점에서의 0,0이되는 값
    printStar(parseInt(N / 2), i, j + parseInt(N / 2));
    printStar(parseInt(N / 2), i + parseInt(N / 2), j);
    printStar(parseInt(N / 2), i + parseInt(N / 2), j + N);
  }
};

printStar(Number(N), 0, 0);
for (value of map) {
  console.log(value.join(""));
}

