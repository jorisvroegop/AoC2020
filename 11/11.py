f = open(r"input.txt", "r")

seats = []
for line in f.readlines():
    line = list(line.rstrip('\n'))
    line = [x.replace("L", "-1") for x in line]
    line = [x.replace(".", "0") for x in line]
    line = [int(x) for x in line]
    seats.append(line)

def check_adjacent(seats: list, row: int, column: int):
    occupied = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            not_itself = not (i == 0 and j == 0)
            lower_limit = (row+i >= 0) and (column+j >= 0)
            upper_limit = (row+i < len(seats)) and (column+j < len(seats[row]))
            if all([not_itself, lower_limit, upper_limit]):
                if seats[row+i][column+j] == 1:
                    occupied += 1
    return occupied

def check_visible(seats: list, row: int, column: int):
    occupied = 0
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if not (i == 0 and j == 0):
                ri, cj = row+i, column+j
                while (0<=ri<len(seats)) and (0<=cj<len(seats[row])):
                    if seats[ri][cj] == 1:
                        occupied += 1
                        break
                    if seats[ri][cj] == -1:
                        break
                    ri += i
                    cj += j
    return occupied

def run_seat_iteration(seats: list, occupy_thresh: int, occupy_rule: str='adjacent'):
    seats_output = [r.copy() for r in seats]
    for r in range(len(seats)):
        for c in range(len(seats[r])):
            if seats[r][c] == 0:
                continue
            if occupy_rule == 'adjacent':
                rule_occupied = check_adjacent(seats, r, c)
            elif occupy_rule == 'visible':
                rule_occupied = check_visible(seats, r, c)
            if (seats[r][c] == -1) and (rule_occupied == 0):
                seats_output[r][c] = 1
            elif (seats[r][c] == 1) and (rule_occupied >= occupy_thresh):
                seats_output[r][c] = -1
    return seats_output

def count_occupied(seats: list):
    return sum(x.count(1) for x in seats)

def find_equilibrium(seats, occupy_thresh, occupy_rule):
    occupied_change, i = 1, 0
    while occupied_change != 0:
        seats_new = run_seat_iteration(seats, occupy_thresh, occupy_rule)
        occupied_change = count_occupied(seats_new) - count_occupied(seats)
        seats = seats_new
        i += 1
        if occupied_change == 0: 
            return f"Equilibrium is found at {count_occupied(seats)} occupied seats after {i-1} iterations."

# Part 1
print(find_equilibrium(seats, 4, 'adjacent'))

# Part 2
print(find_equilibrium(seats, 5, 'visible'))