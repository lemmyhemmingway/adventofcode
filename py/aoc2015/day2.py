SAMPLE_INPUT = [
        [2,3,4],
        [1,1,10]
    ]

FILENAME = "../inputs/2015/day2.txt"


def _parse(filename):
    with open(filename) as f:
        data = f.readlines()

    dimensions = []
    for line in data:
        l,w,h = line.strip().split('x')
        dimensions.append([int(l),int(w),int(h)])

    return dimensions

def part1():
    total = 0
    for item in _parse(FILENAME):
        l,w,h = sorted(item)
        min_area = l * w
        wrapping_paper = 2 * (l*w + w*h + h*l)
        total += min_area + wrapping_paper
    return total

def part2():
    total = 0
    for item in _parse(FILENAME):
        l,w,h = sorted(item)
        ribbon = 2 * (l + w)
        bow = l * w * h
        total += ribbon + bow
    return total


if __name__ == "__main__":
    print("part1")
    print("part2")

