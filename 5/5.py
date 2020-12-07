f = open(r"input.txt", "r")

boarding_passes = []
for line in f.readlines():
    boarding_passes.append(line.rstrip('\n'))

def calc_seat_id(boarding_pass:str):
    x = range(128)
    for i in boarding_pass[:7]:
        h = max(x)+1
        l = min(x)
        m = l+(h-l)//2
        if i == 'F':
            x = range(l, m)
        if i == 'B':
            x = range(m, h)
    row = x.start

    y = range(8)
    for i in boarding_pass[7:]:
        h = max(y)+1
        l = min(y)
        m = l+(h-l)//2
        if i == 'L':
            y = range(l, m)
        if i == 'R':
            y = range(m, h)
    column = y.start
    return row * 8 + column

seat_ids = [calc_seat_id(x) for x in boarding_passes]

print(f"The highest seat ID amongst the boarding passes is {max(seat_ids)}.")

my_seat = [x for x in range(min(seat_ids), max(seat_ids)) if (x not in seat_ids) and (x+1 in seat_ids) and (x-1 in seat_ids)][0]

print(f"{my_seat} is my seat ID.")