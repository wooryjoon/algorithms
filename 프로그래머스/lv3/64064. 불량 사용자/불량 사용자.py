def solution(user_id, banned_id):
    # DFS??
    # 불량 사용자 가능 조건
        # 문자열 길이 동일
        # 별표를 제외한 문자 동일
    # banned_id 1차원 반복, user_id에서 적절한값 찾으면 다음 분기로
    # 종료조건 : depth == banned_id의 길이
    
    ans = 0
    lengths = len(user_id)
    visited = [0] * lengths
    
    def check(banId,userId) :
        ban_length = len(banId)
        user_length = len(userId)
        count = 0
        
        if ban_length != user_length : return False
        for i in range(user_length):
            if banId[i] == '*' :
                count += 1
                continue
            if banId[i] == userId[i] :
                count += 1
        if count == len(banId) : return True
        return False
                
    def DFS (depth) :
        global ans
        
        if depth == len(banned_id) :
            print('yes') 
            return
        for i in range(lengths):
            if visited[i] : continue
            if check(banned_id[depth],user_id[i]) :
                visited[i] = 1
                DFS(depth+1)
                visited[i] = 0
    DFS(0)
    return ans
                