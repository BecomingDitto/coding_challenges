import pytest
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word_parts = []
        for i in range(len(strs[0]), 0, -1):
            first_word_parts.append(strs[0][0:i])

        all_match = False
        for part in first_word_parts:
            for _str in strs:
                if _str.startswith(part):
                    all_match = True
                else:
                    all_match = False
                    break
            if all_match:
                return part
        return ""


class TestSolution:
    def test(self):
        Solution().longestCommonPrefix([""])

    @pytest.mark.parametrize("strings, expected", [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "cat"], ""),
        (["ccc", "cca", "acc"], "")
    ])
    def test_with_params(self, strings, expected):
        assert Solution().longestCommonPrefix(strings) == expected
