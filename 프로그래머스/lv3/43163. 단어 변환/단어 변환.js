function solution(begin, target, words) {
  // 이미바꾸는데 사용한 words는 중복처리
  // 바꾸다가 target이 되는 경우에 멈추고 count를 반환
  // DFS로 각각의 케이스에서 나오는 결과 counting
  let visited = Array.from(Array(words.length), (e) => false);
  let length = begin.length;
  let mincnt = Infinity;
  const DFS = (start, count, visited) => {
    //종료 조건
    if (start === target) {
        console.log(count);
      mincnt = Math.min(mincnt, count);
      return;
    }
    //수행 연산
    for (let i = 0; i < words.length; i++) {
      let sameCount = 0;
      if (visited[i] == false) {
        for (let j = 0; j < length; j++) {
          if (start[j] == words[i][j]) sameCount++;
        }
        if (sameCount == length-1) {
          visited[i] = true;
          DFS(words[i], count + 1, visited);
          visited[i] = false;
        }
      }
    }
  };
  DFS(begin, 0, visited);
  return mincnt == Infinity ? 0 : mincnt;
}
