let [str1, ...str2] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

let ans = [];
// 절대값끼리 값 비교해서 최소힙. 만약에 절대값이 같다면 음수를 올린다.
class Heap {
  constructor() {
    this.heap = [];
  }
  heappush(e) {
    this.heap.push(e);
    this.heapifyUp();
  }
  heapifyUp() {
    let heap = this.heap;
    if (heap.length === 1) return;
    let childIdx = heap.length - 1; // 마지막 노드 자식idx로 설정
    let parentIdx = Math.floor((childIdx - 1) / 2);
    while (childIdx != 0) {
      // 최대로 바뀌는건 childIdx가 루트인덱스가 될 때
      let abschild = Math.abs(heap[childIdx]); // -1
      let absparent = Math.abs(heap[parentIdx]); // 1

      if (abschild < absparent) {
        // 만약 자식이 부모보다 작다면 서로 인덱스 위치 교환
        let temp = heap[childIdx];

        heap[childIdx] = heap[parentIdx];
        heap[parentIdx] = temp;
        childIdx = parentIdx;
        parentIdx = Math.floor((childIdx - 1) / 2);
      } else if (abschild === absparent && heap[childIdx] < heap[parentIdx]) {
        let temp = heap[childIdx];

        heap[childIdx] = heap[parentIdx];
        heap[parentIdx] = temp;
        childIdx = parentIdx;
        parentIdx = Math.floor((childIdx - 1) / 2);
      } else break;
    }
  }
  extractMin() {
    let heap = this.heap;
    if (heap.length === 0) {
      ans.push(0);
      return;
    }
    let returnValue = heap[0];
    let end = heap.pop();
    if (heap.length > 0) {
      heap[0] = end;
      this.heapifyDown();
    }
    ans.push(returnValue);
    return;
  }
  heapifyDown() {
    let heap = this.heap;
    let parentIdx = 0;

    while (true) {
      let leftIdx = 2 * parentIdx + 1;
      let rightIdx = 2 * parentIdx + 2;
      let swap = null;
      let absLeft = Math.abs(heap[leftIdx]);
      let absRight = Math.abs(heap[rightIdx]);
      let absparent = Math.abs(heap[parentIdx]);

      if (
        // 왼쪽자식이 부모보다 절대값이 작거나, 부모랑 절대값이 같은데 실제값이 더 작은경우
        (leftIdx < heap.length && absLeft < absparent) ||
        (leftIdx < heap.length &&
          absLeft === absparent &&
          heap[leftIdx] < heap[parentIdx])
      ) {
        swap = leftIdx;
      }
      if (
        (rightIdx < heap.length && absRight < absparent) ||
        (rightIdx < heap.length &&
          absRight === absparent &&
          heap[rightIdx] < heap[parentIdx])
      ) {
        if (swap === null || (swap != null && absRight < absLeft))
          swap = rightIdx;
        else if (
          swap === null ||
          (swap != null &&
            absRight === absLeft &&
            heap[rightIdx] < heap[leftIdx])
        )
          swap = rightIdx;
      }

      if (swap === null) break; // 자식 둘다 부모보다
      let temp = heap[parentIdx];
      heap[parentIdx] = heap[swap];
      heap[swap] = temp;
      parentIdx = swap;
    }
  }
}
let arr = new Heap();
for (let element of str2) {
  let e = Number(element); // e가 0이 아니라면 e를 힙에 추가 , e가 0 이라면 절대값 최소인것 출력하고 제거

  if (e != 0) arr.heappush(e);
  else {
    arr.extractMin();
  }
}
console.log(ans.join("\n"));
