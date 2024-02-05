import pytest
from unittest.mock import MagicMock
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = [0]
        visited_rooms = set()
        while keys:
            key = keys.pop()
            if self.key_is_for_unvisited_room(key, rooms, visited_rooms):
                keys += rooms[key]
            visited_rooms.add(key)

        return len(visited_rooms) == len(rooms)

    @staticmethod
    def key_is_for_unvisited_room(key, rooms, visited_rooms):
        return (key not in visited_rooms and
                len(rooms) > key >= 0)


class TestSolution:
    def test_initiate(self):
        Solution().canVisitAllRooms(MagicMock())

    @pytest.mark.parametrize("rooms,expected", [
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
        ([[1], [], [3], [4]], False),
        ([[10], [2], []], False),
        ([[2], [0], [1]], True),
        ([[3], [0], [1]], False),
        ([[-3], [0], [1]], False),
        ([[-30], [0], [1]], False),
        ([], False)
    ])
    def test(self, rooms, expected):
        assert Solution().canVisitAllRooms(rooms) is expected
