hour,minute = map(int,input().split())
#입력값의 45분 전 시각을 프린트하게 해주면 됨.
# minute이 45 이상이면 시각을 안바꿔도됨. 분만 -45
# 45 미만이면, hour - 1 해주고, 분은 60 + minute - 45
# 45미만일 때, hour이 0 이면, hour = 23

if minute >= 45 :
    print(hour, minute-45)
else :
    if hour == 0 :
        print('23',60+minute-45)
    else :
        print(hour-1,60+minute-45)