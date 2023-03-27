def solution(id_list, report, k):
    # 신고 무제한 가능
    # 유저당 한번만 신고 가능
    # 신고 기준 넘긴 유저는 대상이 되고,
    # 해당 대상을 신고한 유저에게 알림이 간다.
    answer = []
    reportCountMap = {}
    alarmCountMap = {}
    for x in id_list :
        reportCountMap[x] = set() # 키 먼저 부여
        alarmCountMap[x] = 0
        
    for x in report : # 신고
        reporter,reported = x.split(' ')
        reportCountMap[reported].add(reporter)
        
    for x in reportCountMap:
        if len(reportCountMap[x]) >= k :
            for e in reportCountMap[x]:
                alarmCountMap[e] += 1
    for x in alarmCountMap:
        answer.append(alarmCountMap[x])
    return answer