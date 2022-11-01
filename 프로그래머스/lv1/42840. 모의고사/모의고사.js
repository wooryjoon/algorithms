/*function switch_two (n) {
    let answer;
    switch (n) {
    case 1 : 
    answer = 1;
        break;
    case 2 : 
    answer = 3;
        break;
    case 3 : 
    answer = 4;
        break;
    case 4 : 
    answer = 5;
        break;
    }
    return answer;
}

function switch_three (n) {
    let answer;
    switch (n) {
        case 1:
        case 2:
        answer = 3;
            break;
            
        case 3:
        case 4:
        answer = 1;
            break;
        
        case 5:
        case 6:
        answer = 2;
            break;
            
        case 7:
        case 8:
        answer = 4;
            break;
            
        case 9:
        case 10:
        answer = 5;
            break;
    }
    return answer;
}

function solution(answers) {
    let one_answer = [];
    let two_answer = [];
    let three_answer = [];
    let two_help = 1;
    let three_help = 1;
    let count = [0, 0, 0];
    let answer = [];
    for (let i = 0; i < answers.length; i++) {
        one_answer.push(i % 5 + 1); // 1번 학생
        
        if (i % 2 == 0) two_answer.push(2);
        else {
            two_answer.push(switch_two(two_help));
            two_help++;
            if (two_help == 5) two_help = 1;
        }                           // 2번 학생
        
        three_answer.push(switch_three(three_help));
        three_help++;
        if (three_help == 11) three_help = 1; // 3번 학생
        
    }
    for (i = 0; i < answers.length; i++){
        if (one_answer[i] === answers[i]) count[0]++;
        if (two_answer[i] === answers[i]) count[1]++;
        if (three_answer[i] === answers[i]) count[2]++;
    }
    for (i = 0; i < count.length; i++){
        if (count[i] == Math.max(...count)) answer.push(i+1);
    }
    return answer;
}*/
function solution(answers) {
    let user1 = [1,2,3,4,5];
    let user2 = [2,1,2,3,2,4,2,5];
    let user3 = [3,3,1,1,2,2,4,4,5,5];
    let count = [0,0,0];
    let answer = [];
    for (let i = 0; i < answers.length; i++) {
        if (user1[i % 5] === answers[i]) count[0]++;
        if (user2[i % 8] === answers[i]) count[1]++;
        if (user3[i % 10] === answers[i]) count[2]++;
    }
    let max = Math.max(...count);
    
    for (let i = 0; i < count.length; i++){
        if (count[i] === max) answer.push(i+1); 
    }
    
    return answer;
    
}