import sys
input = sys.stdin.readline
"""
1. 풀이 방법
    #0. 전체 반복문을 시행.
    #1. 키-밸류 형태로 dict에 저장한다.
    #2. 전체 종의 개수를 따로 세준다.
    #3. 반복문이 끝나고 나면 dict의 각 key-value와 total 값을 비교해 비율을 얻는다.
    #4. 소수점 4째자리 어캐함?
"""


total = 0
dic = dict()
while 1:
    word = sys.stdin.readline().rstrip()
    if word == '':
        break
    total += 1
    if word in dic:   # 전에 이미 나왔으면
        dic[word] += 1
    else:
        dic[word] = 1

for property in sorted(dic.items()) :
    key = property[0]
    count = dic[key]
    per = (count / total * 100)
    print("%s %.4f" % (key,per))