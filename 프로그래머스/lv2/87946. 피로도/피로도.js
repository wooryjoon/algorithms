
function solution(k, dungeons) {
    let maxcnt = 0;
    let visited = new Array(dungeons.length).fill(false);
    
    const DFS = (k,count) => {
        maxcnt = Math.max(maxcnt,count);
        //수행연산
        for (let i = 0; i < dungeons.length; i++){
            let [need,cost] = dungeons[i];
            if(visited[i] == false && k >= need) 
            {
                visited[i] = true;
                DFS(k - cost, count+1);
                visited[i] = false; //조합이라면 다시안바꾸겟...지?
        }   
        }
    }
     DFS(k,0);
    return maxcnt;
    }

