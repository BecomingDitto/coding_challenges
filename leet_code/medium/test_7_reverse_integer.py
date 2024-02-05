import pytest


class Solution:
    def reverse(self, x: int) -> int:
        # Check if number is negative, note for the return later
        is_negative = x < 0
        if is_negative:
            x = -x

        reversed_number = 0
        while x > 0:
            x, remainder = divmod(x, 10)
            reversed_number = reversed_number * 10 + remainder

        if is_negative:
            reversed_number = -reversed_number

        if self.out_of_bounds(reversed_number):
            return 0

        return reversed_number

    @staticmethod
    def out_of_bounds(value):
        return value < -2**31 or value > 2**31-1


class TestSolution:
    @pytest.mark.parametrize("number, expected", [
        (123, 321),
        (-123, -321),
        (120, 21),
        (1, 1),
        (-1, -1),
        (1000, 1),
        (2002, 2002),
        (2**32, 0),
        (6463847412, 2147483646),
        (8463847412, 0),
        (-8463847412, -2147483648),
        (-9463847412, 0),
    ])
    def test(self, number, expected):
        assert Solution().reverse(number) == expected