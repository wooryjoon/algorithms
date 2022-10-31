class MPQ {
    constructor(){
        this.values = [];
    }
    insert(element){
        this.values.push(element)
    
    }
    maxBubbleUp(){
    for (let i = 1; i < this.values.length; i++){
        let idx = i;
    while(idx > 0) {
        let parentIdx = Math.floor((idx-1)/2);
        if (this.values[idx] > this.values[parentIdx]){
            let temp;
            temp = this.values[idx];
            this.values[idx] = this.values[parentIdx];
            this.values[parentIdx] = temp;
            idx = parentIdx;
        }
        else break;
        }
    }
    return this.values;
}
    
    minBubbleUp(){
        for (let i = 1; i < this.values.length; i++){
        let idx = i;
    while(idx > 0) {
        let parentIdx = Math.floor((idx-1)/2);
        if (this.values[idx] < this.values[parentIdx]){
            let temp;
            temp = this.values[idx];
            this.values[idx] = this.values[parentIdx];
            this.values[parentIdx] = temp;
            idx = parentIdx;
        }
        else break;
        }
    }
    return this.values;
    }
    
    shift() {
        this.values.shift();
    }
}

function solution(operations) {
    
    let arr = new MPQ();
    let answer = [];
    for (let i = 0; i < operations.length; i++) {
        if (operations[i][0] == 'I'){
            let number = '';
            let idx = operations[i].length-1;
            while (operations[i][idx] != ' '){
                number = operations[i][idx] + number;
                idx--;
            }
            arr.insert(parseInt(number)); 
        }
        else{
            if (operations[i][2] == '1' && arr.values.length != 0) {
                arr.maxBubbleUp();
                arr.shift();
            }
            else if (operations[i][2] == '-' && operations[i][3] == '1' && arr.values.length != 0) {
                arr.minBubbleUp();
                arr.shift();
            }
        }
    }
    if (arr.values.length === 0) return [0,0];
    else {
        arr.maxBubbleUp();
        answer.push(arr.values[0]);
        arr.minBubbleUp();
        answer.push(arr.values[0]);
        return answer;
    }
}