import pytest

class Solution:
    def romanToInt(self, s: str) -> int:
        value_map = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1,

        }
        number = 0
        for symbol, value in value_map.items():
            while s.startswith(symbol):
                s = s[len(symbol):]
                number += value

        return number

class TestSolution:
    def test(self):
        Solution().romanToInt("I")

    @pytest.mark.parametrize("roman, expected", [
        ("I", 1),
        ("III", 3),
        ("IV", 4),
        ("XIV", 14),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ])
    def test_with_params(self, roman, expected):
        assert Solution().romanToInt(roman) == expected
