const input = [];
const strToNumArr = (str) =>
  str.split(" ").map((numString) => Number(numString));

require("readline")
  .createInterface(process.stdin, process.stdout)
  .on("line", function (line) {
    input.push(line.trim());
  })
  .on("close", function () {
    const [N, K] = strToNumArr(input.shift());
    const arr2 = input.map((v) => Number(v));
    let k = Number(K);
    let n = Number(N);

    let count = 0;
    let j = 0;

    for (let i = n - 1; i >= 0; i--) {
      if (k == 0) break;
      money = arr2[i];
      if (parseInt(k / money) == 0) continue;
      else {
        count += parseInt(k / money); // count = 4
        k = k % money; //k = 200 k =
      }
    }

    console.log(count);
  });
