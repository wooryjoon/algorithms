const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim(); 
const taiYear = Number(input);
const gap = 2541 - 1998;
const koreaYear = taiYear - gap;

console.log(koreaYear);
