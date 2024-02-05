import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return self.reverse(x) == x

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
        return value < -2 ** 31 or value > 2 ** 31 - 1


class TestSolution:
    def test(self):
        Solution().isPalindrome(4)

    @pytest.mark.parametrize("number, expected", [
        (0, True),
        (121, True),
        (122, False),
        (-121, False)
    ])
    def test_with_params(self, number, expected):
        assert Solution().isPalindrome(number) == expected

