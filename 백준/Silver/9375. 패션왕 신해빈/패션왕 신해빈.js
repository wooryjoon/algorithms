const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const iterator = input[Symbol.iterator]();
let T = +iterator.next().value;
while (T--) {
  const wear = {};
  let n = +iterator.next().value;
  while (n--) {
    const [ _, kind ] = iterator.next().value.split(/\s+/);
    wear[kind] = (wear[kind] ?? 0) + 1;
  }
  console.log([...Object.values(wear)].reduce((acc, v) => acc*(v+1), 1) - 1);
}