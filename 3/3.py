f = open(r"input.txt", "r")

trees = []
for line in f.readlines():
    line = line.rstrip('\n')
    line = line.replace('.', '0')
    line = line.replace('#', '1')
    line = [int(x) for x in list(line)]
    trees.append(line)

def tree_encounter(trees:list, x_step:int, y_step:int, start_coord=(0,0)):
    # arboreal genetics and biome stability
    n = (len(trees)-y_step) // y_step * x_step // (len(trees[0])-x_step) + 1
    trees = [x * n for x in trees]

    tree_count = 0
    x, y = start_coord
    while y < len(trees) and x < len(trees[0]):
        tree_count += trees[y][x]
        x += x_step
        y += y_step
    return tree_count

print(f"Part 1: With slope (3,1) we encounter {tree_encounter(trees, 3, 1)} trees.")

slopes_to_check = [(1,1), (3,1), (5,1), (7,1), (1,2)]

product = 1
for slope in slopes_to_check:
    x_step, y_step = slope
    product = product * tree_encounter(trees, x_step, y_step)

print(f"Part 2: Product of trees encounters with 5 different slopes: {product}.")