const [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let [poketmon_length, prblms] = str1.split(" ").map(Number);
let map = new Map();
let nameMap = new Map();
let arr = str2.map((e) => e.trim());
let result = [];

for (let i = 0; i < poketmon_length + prblms; i++) {
  if (i < poketmon_length) {
    let value = arr[i];
    // 포켓몬 종류
    map.set(i + 1, value);
    nameMap.set(value, i + 1);
  } else {
    let question = arr[i];
    if (isNaN(Number(question))) {
      result.push(nameMap.get(question));
    } // 문자라는 뜻
    else {
      result.push(map.get(Number(question)));
    }
  }
}
console.log(result.join("\n"));
