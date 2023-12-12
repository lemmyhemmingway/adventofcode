import unittest
from typing import List

INPUT_FILE = "2015/inputs/day5.txt"


def _read_file(input_file: str = INPUT_FILE) -> List[str]:
    data = []
    with open(input_file) as f:
        data = [n.strip("\n") for n in f.readlines()]

    return data


def part1(data):
    total = 0
    for item in data:
        vowel_count = 0
        double_letter = False
        contain_invalid_substring = False
        last_character = ""
        for ch in item:
            if ch in "aeiou":
                vowel_count += 1

            if last_character == ch:
                double_letter = True

            if f"{last_character}{ch}" in ["ab", "cd", "pq", "xy"]:
                contain_invalid_substring = True

            last_character = ch

        if vowel_count >= 3 and double_letter and not contain_invalid_substring:
            total += 1

    return total


def part2(data):
    total = 0
    for item in data:
        has_element = False
        has_index = False

        for index in range(len(item) - 2):
            if f"{item[index]}{item[index+1]}" in item[index + 2 :]:
                has_element = True
            if item[index] == item[index + 2]:
                has_index = True

        if has_element and has_index:
            total += 1

    return total


class TestDay5(unittest.TestCase):
    def test_part1_emtpy_list(self):
        self.assertEqual(0, part1([]))

    def test_part1_only_one_element(self):
        self.assertEqual(1, part1(["aaa"]))

    def test_part1_sample_input(self):
        self.assertEqual(2, part1(["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp"]))

    def test_part1(self):
        self.assertEqual(238, part1(_read_file()))

    def test_part2_empty_list(self):
        self.assertEqual(0, part2([]))

    def test_part2_repeat_characters(self):
        self.assertEqual(1, part2(["qjhvhtzxzqqjkmpb"]))

    def test_part2_sample_input(self):
        self.assertEqual(
            2,
            part2(
                ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
            ),
        )

    def test_part2(self):
        self.assertEqual(69, part2(_read_file()))


if __name__ == "__main__":
    unittest.main()
