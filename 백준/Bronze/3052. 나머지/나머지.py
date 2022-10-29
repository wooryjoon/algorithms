# 10개 입력 받으며
# 각각을 42로 나눈 수를 리스트에 담음
# set함수로 중복 없는 집합을 만듬
# set의 길이 출력
List  = []
for _ in range(10) :
    k = int(input())
    List.append(k % 42)

print(len(set(List))) 