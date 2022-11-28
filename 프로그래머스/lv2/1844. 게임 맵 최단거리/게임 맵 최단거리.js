// function solution(maps) {
// let dx = [0, 1, 0, -1];
// let dy = [1, 0, -1, 0];
// let lengthX = maps.length;
// let lengthY = maps[0].length;
    
//   const BFS = (startNode) => {
//     let queue = [];
//      queue.push(startNode);
//     while (queue.length !== 0) {
//       let currNode = queue.shift();
//         let x = currNode[0];
//         let y = currNode[1];
//         let count =  currNode[2];
//         maps[x][y] = 0;
//         if (maps[lengthX - 1][lengthY - 1] == 0) return count;
//       for (let i = 0; i < 4; i++) {
//         let nx = x + dx[i];
//         let ny = y + dy[i];
//         if (
//           nx >= 0 &&
//           ny >= 0 &&
//           nx < lengthX &&
//           ny < lengthY &&
//           maps[nx][ny] == 1 
//         ) {
//           queue.push([nx, ny,count+1]);
//         }
//       }
//     }
//     return -1;
//   }
    
//   return BFS([0,0,1]);
// }
function solution(maps) {
    const xLength = maps.length;
    const yLength = maps[0].length;
    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];
    
    const bfs = () => {
        const queue = [[0, 0, 1]];
        while (queue.length) {
            const [x, y, count] = queue.shift();
            if (x === xLength - 1 && y === yLength - 1) {
                return count;
            }
            if (maps[x][y]) {
                maps[x][y] = 0;
                dx.forEach((dx, i) => {
                    const nx = x + dx;
                    const ny = y + dy[i];
                    if (nx >= 0 && nx < xLength && ny >= 0 && ny < yLength && maps[nx][ny]) {
                        queue.push([nx, ny, count + 1]);
                    }
                });
            }
        }
        return -1;
    };
    return bfs();
}