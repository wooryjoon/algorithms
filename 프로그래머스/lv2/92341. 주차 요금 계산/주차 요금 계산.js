function solution(fees, records) {
    /*
    fees = [기본시간,기본요금,단위시간,단위요금] ex. [180, 5000, 10, 600]
    records = ["시각 차량번호 내역"] ex. ["05:34 5961 IN"]
    리턴값 : 차량번호가 작은 차부터 청구할 주차요금을 차례대로 정수 배열 담아 리턴
    차량별로 주차된 시간 파악 (Map)
    그 시간을 토대로 fees의 요소들을 이용해 주차요금 계산
    문자열을 받아서 파싱하고, 해당 기록이 IN이라면 1, out이면 0으로 바꾸면서, out일때 
    */
    const car = new Map();
    const answer = [];
    let arr = [];
    const HtoM = (str) => {
        let hour = 60 * parseInt(str[0]+str[1]);
        let min = parseInt(str[3]+str[4]);
        
        return hour + min;
    }
    for (let i = 0; i < records.length; i++){ // 차량번호를 key로 갖는 객체 생성 (오름차순으로 key)
        let carNumber = records[i].split(' ')[1];
        let INOUT =  records[i].split(' ')[2];
        let time = HtoM(records[i].split(' ')[0]);
        
        if (!car.has(carNumber)) car.set(carNumber,0); // 값 : 누적시간, inout상태
        if (INOUT == 'IN') car.set(carNumber,car.get(carNumber)-time);
        else if (INOUT = 'OUT') {
           car.set(carNumber,car.get(carNumber)+time);
        }
    }
    car.forEach((value,key) => { // 출차된 내역이 없는 경우 예외처리
        if (car.get(key) <= 0) {
            return car.set(key,car.get(key)+1439);
        }
    });
    
    for (const array of car.entries()){
        arr.push(array);
    }
    arr.sort((a,b) => a[0] - b[0]); // 차량번호가 낮은 순서대로 비용 계산을 위해 오름차순 정렬
    for (let i = 0; i < arr.length; i++){
        let extraTime = arr[i][1] - fees[0];
        let cost = fees[1];
        if (extraTime > 0) {
            cost = cost + Math.ceil(extraTime / fees[2]) * fees[3];
        }
        answer.push(cost);
    }
    return answer;
    

    
}