const [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let n = Number(str1);
let maps = new Map();
let result = [];

for (let e of str2) {
  let [name, status] = e.trim().split(" ");
  maps.set(name, status);
}
for (let key of maps.keys()) {
  if (maps.get(key) === "enter") result.push(key);
}
result.sort().reverse();
console.log(result.join("\n"));
