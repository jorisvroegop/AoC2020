f = open(r"input.txt", "r")

numlist = []
for line in f.readlines():
    numlist.append(int(line))

print("For n=2 \n")
for x in numlist:
    y = 2020 - x
    if y in numlist:
        print("{} + {} = {}".format(x, y, x+y))
        print("{} * {} = {} \n".format(x, y, x*y))
        break

print("For n=3 \n")
find = False
for x in numlist:
    b = 2020 - x
    for y in numlist:
        z = b - y   
        if (y in numlist) and (z in numlist):
            print("{} + {} + {} = {}".format(x, y, z, x+y+z))
            print("{} * {} * {} = {} \n".format(x, y, z, x*y*z))
            find = True
            break
    if find:
        break