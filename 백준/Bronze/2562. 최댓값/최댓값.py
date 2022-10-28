answers = []
for _ in range(9) :
    i = int(input())
    answers.append(i)

print(max(answers))
print(answers.index(max(answers))+1)
