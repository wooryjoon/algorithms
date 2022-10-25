const fs = require("fs");

const id = fs.readFileSync("/dev/stdin").toString().trim();

console.log(`${id}??!`);
