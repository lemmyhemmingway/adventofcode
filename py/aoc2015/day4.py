import hashlib

SAMPLE_INPUT = "ckczppom"

def part1():
    num = 0
    while True:
        text = f'{SAMPLE_INPUT}{num}'
        result = hashlib.md5(text.encode()).hexdigest()
        if result[0:5] == "00000":
            break
        num += 1

    return num

def part2():
    num = 0
    while True:
        text = f'{SAMPLE_INPUT}{num}'
        result = hashlib.md5(text.encode()).hexdigest()
        if result[0:6] == "000000":
            break
        num += 1

    return num


if __name__ == "__main__":
    print(part1())
    print(part2())
