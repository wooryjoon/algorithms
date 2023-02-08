const [N, ...arr] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let casesLength = Number(N);
const extractHigh = (dist) => {
  let accDist = 0;
  for (let i = 1; i <= dist; i++) {
    accDist += i;
    if (accDist - i > dist - accDist) {
      return i - 1;
    }
  }
};

for (let i = 0; i < casesLength; i++) {
  let [from, to] = arr[i].split(" ").map(Number);
  let distance = Math.abs(to - from);
  if (distance === 1) {
    console.log(1);
    continue;
  }
  let peak = extractHigh(distance);
  let count = 2 * peak - 1;
  let currDist = peak;
  for (let j = 0; j < peak; j++) {
    currDist += 2 * j;
  }
  if (currDist === distance) {
    console.log(count);
  } else if (distance - currDist <= peak) {
    console.log(count + 1);
  } else {
    console.log(count + 2);
  }
}
