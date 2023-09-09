SAMPLE_INPUT = [
        '(',
        ')',
        ')',
]

FILENAME = "../inputs/2015/day1.txt"

def _parse(filename):
    with open(filename) as f:
        data = f.read()
    return data

def part1():
    floor = 0
    for item in _parse(FILENAME):
        if item == '(':
            floor += 1
        elif item == ')':
            floor -= 1
    return floor


def part2():
    position = 0
    floor = 0
    for item in _parse(FILENAME):
        if item == '(':
            floor += 1
        elif item == ')':
            floor -= 1

        if floor == -1:
            break
        position += 1
    return position

if __name__ == "__main__":
    p1 = part1()
    print(p1)
    p2 = part2()
    print(p2)
