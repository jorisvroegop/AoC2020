f = open(r"input.txt", "r")

answers = []
answer = []
for line in f.readlines() + ['\n']:
    if line == '\n':
        answers.append([list(x) for x in answer])
        answer = []
        continue
    line = line.rstrip('\n')
    answer.append(line)

def calc_group_set(group:list, part:int):
    answer_set = set()
    for x, i in enumerate(group):
        if x == 0:
            answer_set = set(i)
        if part==1:
            answer_set = answer_set.union(set(i))
        if part==2:
            answer_set = answer_set.intersection(set(i))
    return answer_set

no_of_yes_q1 = [len(calc_group_set(group, 1)) for group in answers]

print(f"The total sum of the yes answered questions per group is {sum(no_of_yes_q1)}.")

no_of_yes_q2 = [len(calc_group_set(group, 2)) for group in answers]

print(f"The total sum of the unanimously yes answered questions per group is {sum(no_of_yes_q2)}.")
