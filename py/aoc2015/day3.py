SAMPLE_INPUT = "^>v<"

FILENAME = "../inputs/2015/day3.txt"


def _parse(filename):
    with open(filename) as f:
        data = f.read()

    return data.strip()


def part1():
    visited_locations = set()
    x = 0
    y = 0
    for ch in _parse(FILENAME):
        if ch == "^":
            y += 1
        elif ch == ">":
            x += 1
        elif ch == "<":
            x -= 1
        elif ch == "v":
            y -= 1
        visited_locations.add((x, y))

    return len(visited_locations)


def part2():
    general_visited_locations = set()
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    for key, ch in enumerate(_parse(FILENAME)):
        if key % 2 == 0:
            if ch == "^":
                robo_y += 1
            elif ch == ">":
                robo_x += 1
            elif ch == "<":
                robo_x -= 1
            elif ch == "v":
                robo_y -= 1
            general_visited_locations.add((robo_x, robo_y))

        else:
            if ch == "^":
                santa_y += 1
            elif ch == ">":
                santa_x += 1
            elif ch == "<":
                santa_x -= 1
            elif ch == "v":
                santa_y -= 1
            general_visited_locations.add((santa_x, santa_y))

    return len(general_visited_locations)

            


if __name__ == "__main__":
    print(part1())
    print(part2())
