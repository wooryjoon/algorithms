const input = require("fs")
  .readFileSync("dev/stdin")
  .toString()
  .trim()
  .split("\n");
str = input[0].split(" ");
if (str[0] === "") {
  console.log(0);
  return;
}

console.log(str.length);
