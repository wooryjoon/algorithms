const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

input.shift();
// 삽입정렬

for (let i = 1; i < input.length; i++) {
  for (let j = i; j >= 1; j--) {
    if (input[j] < input[j - 1]) {
      let temp = input[j];
      input[j] = input[j - 1];
      input[j - 1] = temp;
    }
  }
}
input.map((e) => {
  console.log(e);
});
