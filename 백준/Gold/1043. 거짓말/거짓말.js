/*
아이디어
  파티에서 최대한 거짓말을 하고싶다
  근데 파티에 참석한 인원중 진실을 아는 사람이 있으면 진실을 말해야한다
  어떤 파티에서 진실을 듣고 다른 파티에서 거짓말을 들으며 거짓말쟁이가된다
  for x in party
    if trueman 중 하나라도 in x:
      진실을 말한다.
      x의 원소 모두 trueman 목록에추가
    else count ++ 거짓말 가능한 파티 카운트 ++
          
시간복잡도

변수 설정
*/

const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [n, m] = input[0].split(" ").map(Number); // 사람 수, 파티 수
let [length, ...trueMan] = input[1].split(" ").map(Number); // 진실아는사람
let party = [];
let set = new Set(trueMan);
let ans = 0;

for (let i = 0; i < m; i++) {
  let [length, ...people] = input[i + 2].split(" ").map(Number);
  let flag = false;
  party.push(people);
}

for (let i = 0; i < m; i++) {
  for (let members of party) {
    let flag = false;
    for (let member of members) {
      if (set.has(member)) {
        flag = true;
        break;
      }
    }
    if (flag === true) set = new Set([...set, ...members]);
  }
}
for (let members of party) {
  let flag = false;
  for (let member of members) {
    if (set.has(member)) {
      flag = true;
      break;
    }
  }
  if (flag === false) ans += 1;
}
console.log(ans);
