def solution(today, terms, privacies):
    """
    오늘 날짜, 약관 정보 (유효기간), 정보의 수집 날짜와 약관 타입이 주어질 때, 
    각 정보들이 오늘 날짜를 기준으로 초과된 정보들의 번호를 오름차순으로 담아 반환
    
    [풀이 방법]
    1. terms 를 분해해서 termMap을 만든다. termMap[term] = 해당 term의 약관 유효 기간
    2. privacie를 분해해서 year, month, day, type을 얻는다.
    3. 그후 termMap[type]의 값에 따라 날짜를 더해주고, today보다 작다면 answer에 i+1을 담는다.
    4. 반복문이 종료된 후 answer를 리턴한다.
    """
    answer = []
    termMap = dict()
    year_today, month_today, day_today = map(int,today.split('.'))
    today = year_today * 28 * 12 + month_today * 28 + day_today
    # terms 를 분해해서 termMap을 만든다.
    for e in terms:
        type, duration = e.split()
        termMap[type] = duration
    # privacie를 분해해서 year, month, day, type을 얻는다.
    for number in range(len(privacies)):
        time, type = privacies[number].split(' ')
        year,month,day = map(int,time.split('.'))
        addMonth = int(termMap[type])
        year += (addMonth // 12) # 우선 년 수 더하기
        month = month + addMonth % 12
        if month > 12 :
            month = month % 12
            year += 1

        expireDate = year * 28 * 12 + month * 28 + day
        if expireDate <= today : answer.append(number+1)
    return answer