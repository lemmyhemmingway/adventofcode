import unittest

input_file = "2015/inputs/day1.txt"


def _read_input_file(input_file: str = input_file) -> str:
    data = ""
    with open(input_file) as f:
        data = f.read()

    return data


def part1(data):
    position = 0
    for c in data:
        if c == "(":
            position += 1
        elif c == ")":
            position -= 1

    return position


def part2(data):
    position = 0
    index = 0
    for c in data:
        if c == "(":
            position += 1
        elif c == ")":
            position -= 1
        index += 1

        if position == -1:
            break

    return index


class TestDay1(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(74, part1(_read_input_file()))

    def test_part1_sample_input(self):
        self.assertEqual(1, part1("("))

    def test_part1_empty_input(self):
        self.assertEqual(0, part1(""))

    def test_part2_empty_input(self):
        self.assertEqual(0, part2(""))

    def test_part2_sample_input(self):
        self.assertEqual(1, part2(")"))

    def test_part2(self):
        self.assertEqual(1795, part2(_read_input_file()))


if __name__ == "__main__":
    unittest.main()
