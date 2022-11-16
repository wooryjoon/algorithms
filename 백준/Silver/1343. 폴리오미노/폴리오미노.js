const inputData = require("fs").readFileSync("/dev/stdin").toString().trim();

let board = inputData.replace(/XXXX/g, "AAAA").replace(/XX/g, "BB");

if (board.includes("X")) {
  console.log(-1);
} else {
  console.log(board);
}