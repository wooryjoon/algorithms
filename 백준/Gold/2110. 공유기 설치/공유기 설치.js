const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")

let [N, C] = input[0].trim().split(" ").map(Number) // 집 개수, 공유기 개수
let location = []
for (let i = 1; i < input.length; i++) {
  location.push(Number(input[i].trim()))
}
location.sort((a, b) => a - b)
let left = 0
let right = location[N - 1]
let ans = -1

// 가장 인접한 공유기 사이의 최단거리 구하기
// 공유기 사이의 최단거리 후보 완전 탐색 -> 이분 탐색

while (left <= right) {
  mid = parseInt((left + right) / 2) // 현재 설정한 최단거리
  count = 1 // 설치한 공유기 갯수. (맨 앞에 바로 하나 설치했다고 가정)
  currLoc = location[0] // 가장 최근 공유기 위치
  for (let i = 1; i < N; i++) {
    if (location[i] - currLoc >= mid) {
      // 다음 설치할 위치와 현재 공유기 위치의 거리가 mid보다 크면 설치
      count++
      currLoc = location[i]
    }
  }
  if (count < C) right = mid - 1
  else if (count >= C) {
    // 현재 최단거리로 모든 공유기 설치 가능하다. 좀 더 넓혀도 됌.
    left = mid + 1
    ans = mid
  }
}
console.log(ans)
