def part1():
    result = 0
    dimensions = read_file_to_list()
    for dimension in dimensions:
        l, w, h = dimension
        sides = [l * w, w * h, h * l]
        result += 2 * l * w + 2 * w * h + 2 * h * l + min(sides)

    print(result)

def part2():
    result = 0
    dimensions = read_file_to_list()
    for dimension in dimensions:
        sorted_dimension = sorted(dimension)
        l, w, h = sorted_dimension
        result += 2 * l + 2 * w + l * w * h

    print(result)

def read_file_to_list():
    with open('../inputs/day2.txt') as file:
        data = file.readlines()

    inputs = []
    for line in data:
        l, w, h = line.strip().split('x')
        inputs.append([int(l), int(w), int(h)])

    return inputs



if __name__ == "__main__":
    part1()
    part2()


