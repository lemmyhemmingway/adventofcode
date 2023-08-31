with open("inputs/day1.txt") as f:
    data = f.read()


def part1():
    floor = 0
    for ch in data:
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
    return floor

def part2():
    floor = 0
    position = 0
    for ch in data:
        if ch == '(':
            floor += 1
        elif ch == ')':
            floor -= 1
        position += 1

        if floor == -1:
            return position
    return floor



if __name__ == "__main__":
    print(part1())
    print(part2())
