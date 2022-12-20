const N = require("fs").readFileSync("/dev/stdin").toString().trim();

stars = [];
const recur = (n, i, j) => {
  if (i % 3 == 1 && j % 3 == 1) {
    // 기본 조건
    stars.push(" ");
    return;
  } else if (n == 1) {
    // 재귀의 base에 도달했을때까지 위조건 만족 안될시 별
    stars.push("*");
    return;
  }
  recur(Math.floor(n / 3), Math.floor(i / 3), Math.floor(j / 3));
  // base에 도달하지 않았고, 중간에 공백처리 안됐으면 재귀타고드감
};

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    recur(N, i, j);
  }
  stars.push("\n");
}

console.log(stars.join("").trim());
