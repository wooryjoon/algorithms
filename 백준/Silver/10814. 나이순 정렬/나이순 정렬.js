const [n, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let newArr = [];
for (let str of arr) {
  let temp = str.split(" ");
  newArr.push(temp);
}
newArr.sort((a, b) => {
  if (a[0] != b[0]) return a[0] - b[0];
  if (a[0] == b[0]) {
    return a[1][0] - b[1][0];
  }
});
for (let i = 0; i < newArr.length; i++) {
  newArr[i] = newArr[i].join(" ");
}

for (let e of newArr) {
  console.log(e);
}
