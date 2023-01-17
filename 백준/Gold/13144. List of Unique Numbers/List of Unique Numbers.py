n = int(input())
s = list(map(int,input().split()))
re=0
st,en = 0,0
ch = [False]*100001
while st!=n and en!=n:#시작 지점과 끝나는 지점이 n이면 멈춰줌 
    if not ch[s[en]]:#끝나는 지점이 안 나온 수 라면 앞으로 전진해줌
        ch[s[en]]=True
        en+=1
        re+=en-st#s=[1, 2, 3]인 경우 st = 0,en=1,2,3|en =1: 1, en = 2: 1 2/ 2, en = 3: 1 2 3/ 2, 3/ 3
    else:
        while ch[s[en]]:#s[en]이 참인 경우 = 앞에 중복되는 숫자가 이미 나왔다.
            ch[s[st]]=False#앞에 나온 숫자는 이제 안 쓸거므로 False로 바꿔줌
            st+=1#다음 숫자로 이동
    
print(re)#결과 출력