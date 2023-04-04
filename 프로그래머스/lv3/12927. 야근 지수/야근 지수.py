from heapq import heappush, heappop
def solution(n, works):
		# 남아있는 n시간 동안 works 배열에 담긴 원소를 어떻게 빼줄것인가?
		# 제곱 합을 최대로 만들기 위해서는 works 배열의 값을 최대한 모두 비슷하게 만들어준다.
    # 이를 위해 works 배열 원소의 최대값을 1씩 빼주는 연산을 n번 반복
		# 매 반복마다 배열의 최대값을 효율적으로 구하기 위해 우선순위 큐 활용
    answer = 0
    pq = [] # 우선순위 큐

    if sum(works) <= n : return 0 # 예외 처리 (퇴근 전까지 일을 모두 끝내는 케이스)

    for e in works: # 힙에 works 배열 요소를 모두 넣는 연산
				# heappush를 통해 push + heapify(힙정렬)
				# 원소의 값을 음수로 변환시켜 넣는 이유는 최소힙을 최대힙처럼 활용하기 위해.
        heappush(pq,-e)  # 최소 힙. 최대값.
		# -> O(logN)

    for i in range(n):
        temp = -heappop(pq) - 1 # 힙에서 최소값을 꺼내 양수로 변환시키고, 1 빼기
        heappush(pq,-temp) # 결과값을 다시 힙에 넣기
		# -> O(N * logN) 

    for e in pq :
        answer += e ** 2
		# -> O(N)

		# 최종 시간 복잡도 : O(NlogN)
    return answer

# Review
# 	제곱합이 최소가 되려며 어떤 식으로 빼주어야 하는지,
# 	매 분기마다 최대값을 도출하기 위해 '우선순위 큐' 활용


#### max메서드와 index 메서드를 활용해 무식하게 구하는 방법 ####

# from heapq import heappush, heappop
# def solution(n, works):
#     # 남아있는 n시간 동안 works 배열에 담긴 원소를 어떻게 빼줄것인가?
#     # 제곱 합을 최소로 만들기 위해서는 works 배열의 값을 최대한 모두 비슷하게 만들어준다.
#     # 이를 위해 works 배열의 최대값을 1씩 빼주는 연산을 n번 반복
#     # max메서드와 index메서드를 활용

#     answer = 0 # 출력할 정답 변수
#     if sum(works) <= n : return 0 # 미리 예외처리
#     for _ in range(n):
#         currMaxIndex = works.index(max(works)) # 현재 works 배열에서 가장 최대인 값의 위치
#         works[currMaxIndex] -= 1
        
#     for e in works:
#         answer += e ** 2
#     return answer
		# -> 시간복잡도 : O(n^3)