from typing import List
import unittest

INPUT_FILE = "2015/inputs/day2.txt"


def _read_input(input_file: str = INPUT_FILE):
    data = []
    with open(input_file) as file:
        data = [
            [int(x) for x in item.strip("\n").split("x")] for item in file.readlines()
        ]
    return data

def part1(data: List[List[int]]) -> int:
    total = 0
    for item in data:
        l, h, w = sorted(item)
        paper = 2 * ((l * h) + (h * w) + (l * w))
        slack = l * h
        total += paper + slack

    return total


def part2(data: List[List[int]]) -> int:

    total = 0
    for item in data:
        l, h, w = sorted(item)
        wrap = l * w * h
        ribbon = 2 * l + 2 * h
        total += wrap + ribbon

    return total


class TestDay2(unittest.TestCase):
    def test_part1_empty_input(self):
        self.assertEqual(0, part1([]))

    def test_part1_sample_input(self):
        self.assertEqual(58, part1([[2, 3, 4]]))

    def test_part1(self):
        self.assertEqual(1598415, part1(_read_input()))

    def test_part2_emtpy_input(self):
        self.assertEqual(0, part2([]))

    def test_part2_sample_input(self):
        self.assertEqual(34, part2([[2, 3, 4]]))

    def test_part2(self):
        self.assertEqual(3812909, part2(_read_input()))


if __name__ == "__main__":
    unittest.main()
