import unittest

INPUT_FILE = "2015/inputs/day3.txt"


def _read_file(input_file: str = INPUT_FILE) -> str:
    with open(input_file) as f:
        data = f.read()

    return data


def part1(data: str) -> int:
    visited = {(0, 0)}
    x = 0
    y = 0

    for ch in data:
        if ch == "^":
            y += 1
        elif ch == ">":
            x += 1
        elif ch == "v":
            y -= 1
        elif ch == "<":
            x -= 1
        visited.add((x, y))

    return len(visited)


def part2(data: str) -> int:
    santa_x = 0
    santa_y = 0
    robot_x = 0
    robot_y = 0
    santa_location = {(santa_x, santa_y)}

    for key, ch in enumerate(data):
        if key % 2 == 0:
            if ch == "^":
                santa_y += 1
            elif ch == ">":
                santa_x += 1
            elif ch == "v":
                santa_y -= 1
            elif ch == "<":
                santa_x -= 1
            santa_location.add((santa_x, santa_y))
        else:
            if ch == "^":
                robot_y += 1
            elif ch == ">":
                robot_x += 1
            elif ch == "v":
                robot_y -= 1
            elif ch == "<":
                robot_x -= 1
            santa_location.add((robot_x, robot_y))

    return len(santa_location)


class TestDay3(unittest.TestCase):
    def test_part1_empyt_input(self):
        self.assertEqual(1, part1(""))

    def test_part1_sample_input(self):
        self.assertEqual(2, part1(">"))

    def test_part1(self):
        self.assertEqual(2565, part1(_read_file()))

    def test_part2_empty_input(self):
        self.assertEqual(1, part2(""))

    def test_part2_sample_input(self):
        self.assertEqual(11, part2("^v^v^v^v^v"))

    def test_part2(self):
        self.assertEqual(2639, part2(_read_file()))


if __name__ == "__main__":
    unittest.main()
