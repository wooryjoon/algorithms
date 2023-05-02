def solution(dirs):
    # 11*11 2차원 배열 생성 후, (5,5) 에서 시작.
    #dict[5556] 이런 식으로 중복 체크해보자
    ans = set()
    visited = [[0]*11 for _ in range(11)]
    x= 5
    y= 5
    dict = {
        'U' : [-1,0],
        'D' : [1,0],
        'R' : [0,1],
        'L' : [0,-1]
    }
    arr = list(dirs)
    for e in arr :
        dx,dy = dict[e]
        nx,ny = x+dx,y+dy
        if not ((0<=nx<=10) and (0<=ny<=10)): continue
        ans.add(''.join(map(str,[x,y,nx,ny])))
        ans.add(''.join(map(str,[nx,ny,x,y])))
        x = nx
        y = ny
    print(ans)
    return len(ans)//2