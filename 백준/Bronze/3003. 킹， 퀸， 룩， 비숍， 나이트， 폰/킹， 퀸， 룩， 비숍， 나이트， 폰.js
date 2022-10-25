const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");
let answer = [1, 1, 2, 2, 2, 8];
let mine = [];
let mine_str = "";

for (let i = 0; i < answer.length; i++) {
  mine[i] = answer[i] - input[i];
}

for (let i = 0; i < mine.length; i++) {
    mine_str += mine[i].toString()+ ' ';
}
console.log(mine_str.trim());