def solution(people, limit):
    ans = 0
    people.sort(reverse=True)
    left = 0
    right = len(people)-1
    
    while left <= right :
        if people[left] + people[right] > limit :
            left += 1
        else :
            left +=1
            right -=1
        ans +=1
    
                
    return ans