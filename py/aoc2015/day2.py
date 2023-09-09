SAMPLE_INPUT = [[2, 3, 4], [1, 1, 10]]

FILENAME = "../inputs/2015/day2.txt"


def _parse(filename):
    with open(filename) as f:
        data = f.readlines()

    dimensions = []
    for line in data:
        length, width, height = line.strip().split("x")
        dimensions.append([int(length), int(width), int(height)])

    return dimensions


def part1():
    total = 0
    for item in _parse(FILENAME):
        length, width, height = sorted(item)
        min_area = length * width
        wrapping_paper = 2 * (length * width + width * height + height * length)
        total += min_area + wrapping_paper
    return total


def part2():
    total = 0
    for item in _parse(FILENAME):
        length, width, height = sorted(item)
        ribbon = 2 * (length + width)
        bow = length * width * height
        total += ribbon + bow
    return total


if __name__ == "__main__":
    print("part1")
    print("part2")
