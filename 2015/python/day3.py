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
    return 0



class TestDay3(unittest.TestCase):
    def test_part1_empyt_input(self):
        self.assertEqual(1, part1(""))

    def test_part1_sample_input(self):
        self.assertEqual(2, part1(">"))

    def test_part1(self):
        self.assertEqual(2565, part1(_read_file()))

    def test_part2_empty_input(self):
        self.assertEqual(0, part2(""))

    def test_part2_sample_input(self):
        self.assertEqual(3, part2("^v"))


if __name__ == "__main__":
    unittest.main()
