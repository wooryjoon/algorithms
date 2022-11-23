let [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let cityAndPeople = arr.map((i) => i.split(" ").map((j) => +j));

function sol(n, cityAndPeople) {
  let people = 0;
  let total = 0;
  //마을의 위치를 기준으로 오름차순 정렬 후, 전체 인구의 절반을 넘는 그 순간의 마을 번호를 출력.
  cityAndPeople.sort((a, b) => a[0] - b[0]); // 오름차순 정렬
  total = cityAndPeople.reduce((acc, cur) => acc + cur[1], 0);
  let half = total / 2;
  for (let i = 0; i < cityAndPeople.length; i++) {
    people += cityAndPeople[i][1];
    if (people >= half) {
      return cityAndPeople[i][0];
    }
  }
  return cityAndPeople[cityAndPeople.length - 1][0];
}

console.log(sol(n, cityAndPeople));
