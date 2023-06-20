import copy
def solution(user_id, banned_id):
    # DFS
    # 불량 사용자 가능 조건
        # 문자열 길이 동일
        # 별표를 제외한 문자 동일

    ans = set()
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

    def DFS (depth,banList) :
        if depth == len(banned_id) :
            newArr = sorted(banList)
            ans.add(''.join(newArr))
            return

        for i in range(lengths):
            if visited[i] : continue
            if check(banned_id[depth],user_id[i]) :
                visited[i] = 1
                banList.append(user_id[i])
                DFS(depth+1,banList)
                visited[i] = 0
                banList.pop()
    DFS(0,[])
    return(len(ans))