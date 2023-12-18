// 3. 여러 줄의 값들을 입력받을 때
const [a, b] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let [N, M] = a.split(" ").map(Number); // 애들 수 , 과자 수
let lengths = b
  .split(" ")
  .map(Number)
  .sort((a, b) => a - b);

/* 
N명의 조카에게 모두 같은 길이의 과자를 줘야함
근데 줄수 있는 최대 길이를 구하라
과자 길이의 배열 원소중 하나가 될것이고, 선형탐색 대신 이분탐색
조건을 만족하더라도, 최대값을 찾아야 하므로 upper bound? 활용
조건을 만족할 때 : 현재 인덱스부터 해서 유효한 원소가 N개 이상 있으면 만족
구하고자 하는 것 : 과자의 최대 길이
*/
let left = 0;
let right = Math.max(...lengths);
let result = 0;

while (left <= right) {
  let mid = Math.floor((left + right) / 2);
  let count = 0;
  for (let i = 0; i < M; i++) {
    count += Math.floor(lengths[i] / mid); // 피봇으로 잡은 길이로 각 과자를 나눈 몫을 합한다.
  }
  if (count >= N) {
    // 그렇게 해서 나온 몫의 합이 아이 수보다 많거나 같다? -> 길이를 더 늘려서 가능한 애들 수를 줄여도 된다
    left = mid + 1;
    result = mid;
  } else {
    // 그게 아니라 애들 수보다 더 작으면, 길이를 좀 줄여야 한다 피봇 범위 더 작은 곳에서 탐색
    right = mid - 1;
  }
}
console.log(result);
