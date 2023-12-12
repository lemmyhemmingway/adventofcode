import unittest
import hashlib


def part1(data: str) -> int:
    i = 0
    while True:
        result = hashlib.md5(f"{data}{i}".encode())
        output = result.digest()
        if output.hex().startswith("00000"):
            break
        i += 1

    return i


def part2(data: str) -> int:
    i = 0
    while True:
        result = hashlib.md5(f"{data}{i}".encode())
        output = result.digest()
        if output.hex().startswith("000000"):
            break
        i += 1

    return i


class TestDay4(unittest.TestCase):
    def test_part1_sample(self):
        self.assertEqual(609043, part1("abcdef"))

    def test_part1_second_sample(self):
        self.assertEqual(1048970, part1("pqrstuv"))

    def test_part1(self):
        self.assertEqual(117946, part1("ckczppom"))

    def test_part2(self):
        self.assertEqual(3938038, part2("ckczppom"))


if __name__ == "__main__":
    unittest.main()
