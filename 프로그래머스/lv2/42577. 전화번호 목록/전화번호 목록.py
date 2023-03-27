def solution(phone_book):
    answer = True
    hashMap = {}
    for x in phone_book:
        hashMap[x] = 1
    for number in phone_book:
        temp = ''
        for x in number:
            temp += x
            if temp in hashMap and temp != number:
                answer = False
                break
    return answer