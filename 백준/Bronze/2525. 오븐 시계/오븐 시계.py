hour,minute = map(int,input().split())
time = int(input())
hPlus = time // 60
mPlus = time % 60

if minute+mPlus >= 60 :
    if hour+hPlus+1 >= 24 :
        print(hour+hPlus+1 - 24, minute+mPlus-60)
    else :
        print(hour+hPlus+1,minute+mPlus-60)
else :
    if hour+hPlus >= 24 :
        print(hour+hPlus-24, minute+mPlus)
    else :
        print(hour+hPlus,minute+mPlus)
