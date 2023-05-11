def solution(n, lost, reserve):
    answer = 0
    # n == 5 : [1,2,3,4,5]
    # 앞 / 뒤로만 여벌 옷 전달 가능.
    # 우선, 코드 치기 전에 각각 학생이 보유한 옷의 개수를 구하기.
    clothes = [1] * (n+1)
    for e in lost :
        clothes[e] -= 1
    for e in reserve:
        clothes[e] += 1
    clothes[0] = False
    
    for i in range(1,n+1):
        if clothes[i] >= 1 :
            answer += 1
            continue
            
        if i > 1 and clothes[i] == 0 and clothes[i-1] >= 2 :
            answer += 1
            clothes[i] += 1
            clothes[i-1] -= 1
            
        elif i < n and clothes[i] == 0 and clothes[i+1] >= 2 :
            answer += 1
            clothes[i] +=1
            clothes[i+1] -= 1
            
        
    return answer