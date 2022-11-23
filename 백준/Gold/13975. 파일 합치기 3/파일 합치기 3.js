//배열의 최소값 두개를 빼고 합쳐 새로운 값을 만들고, 그걸 다시 배열에넣는다.
//우선순위큐 최소힙으로 풀면 될듯.

// 5. 첫 번째 줄에 자연수 n을 입력받고, 그 다음줄부터 n개의 줄에 걸쳐 한 줄에 하나의 값을 입력받을 때
class MinHeap {
  constructor() {
    this.heap = [null];
  }

  size() {
    return this.heap.length - 1;
  }

  getMin() {
    return this.heap[1] ? this.heap[1] : null;
  }

  swap(a, b) {
    [this.heap[a], this.heap[b]] = [this.heap[b], this.heap[a]];
  }

  heappush(value) {
    this.heap.push(value);
    let curIdx = this.heap.length - 1;
    let parIdx = (curIdx / 2) >> 0;

    while (curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
      this.swap(parIdx, curIdx);
      curIdx = parIdx;
      parIdx = (curIdx / 2) >> 0;
    }
  }

  heappop() {
    const min = this.heap[1];
    if (this.heap.length <= 2) this.heap = [null];
    else this.heap[1] = this.heap.pop();

    let curIdx = 1;
    let leftIdx = curIdx * 2;
    let rightIdx = curIdx * 2 + 1;

    if (!this.heap[leftIdx]) return min;
    if (!this.heap[rightIdx]) {
      if (this.heap[leftIdx] < this.heap[curIdx]) {
        this.swap(leftIdx, curIdx);
      }
      return min;
    }

    while (
      this.heap[leftIdx] < this.heap[curIdx] ||
      this.heap[rightIdx] < this.heap[curIdx]
    ) {
      const minIdx =
        this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
      this.swap(minIdx, curIdx);
      curIdx = minIdx;
      leftIdx = curIdx * 2;
      rightIdx = curIdx * 2 + 1;
    }

    return min;
  }
}
const arr = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
let T = arr[0];
let num_arr = [];
let size_arr = [];

for (let i = 1; i <= 2 * T; i++) {
  if (i % 2 == 1) {
    num_arr.push(Number(arr[i]));
  } else {
    size_arr.push(arr[i].split(" ").map(Number));
  }
}

for (let i = 0; i < T; i++) {
  let PQ = new MinHeap();
  let sum = 0;
  let add = 0;
  for (let j = 0; j < size_arr[i].length; j++) {
    PQ.heappush(size_arr[i][j]); // 각각의원소를 enqueue하면서 자동 힙정렬
  }

  while (PQ.heap.length !== 2) {
    add = 0;
    add += PQ.heappop();
    add += PQ.heappop();
    sum += add;

    PQ.heappush(add);
  }
  console.log(sum);
}
