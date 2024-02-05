import pytest
import bisect
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        self.check_constraints(nums, target)
        sorted_nums = sorted(nums.copy())
        diff_from_target, base_sum = self.initial_values(sorted_nums, target)






        sums = self.compute_sum_pairs(sorted_nums)
        sum_keys = list(sums.keys())
        best_attempt = None
        for i, num in enumerate(sorted_nums):
            diff_from_target = target - num
            index = bisect.bisect(sum_keys, diff_from_target)
            # Now we just need to check the area.  We'll check index, index - 1 and index + 1,
            # as that should get us as close to the target as possible.

            closest_sum = self.get_closest_sum(index, num, sum_keys, target)
            if closest_sum == target:
                return closest_sum

            if best_attempt is None or \
                    (best_attempt is not None and
                     abs(target - closest_sum) < abs(target - best_attempt)
                    ):
                best_attempt = closest_sum

        return self.find_closest(nums, target)

    def initial_values(self, nums, target):
        sum = nums[0]+nums[1]+nums[2]
        diff = abs(target-sum)




    def get_closest_sum(self, index, num, sum_keys, target):
        for j in [index - 1, index, index + 1]:
            try:
                tmp_value = sum_keys[j] + num


            except IndexError:
                pass
        return 5

    @staticmethod
    def compute_sum_pairs(nums):
        two_sums = {}
        try:
            for i, first in enumerate(nums, 0):
                for j, second in enumerate(nums[i+1:], i+1):
                    _sum = first + second
                    if _sum not in two_sums:
                        two_sums[_sum] = []
                    two_sums[_sum].append([i, j])

        except IndexError:
            pass
        return two_sums
    #
    # @staticmethod
    # def find_closest_three_sum(sums, nums, target):
    #     # Just need to start with something valid.  The rest will shake out.
    #     closest_sum = nums[0] + nums[1] + nums[2]
    #     smallest_diff_from_target = abs(target - closest_sum)
    #
    #     for _sum in sums:
    #         for i, num in enumerate(nums):
    #             if _sum.index_used(i):
    #                 pass
    #             three_sum = _sum.sum + num
    #             diff_from_target = abs(target - three_sum)
    #             if diff_from_target < smallest_diff_from_target:
    #                 closest_sum = three_sum
    #
    #     return closest_sum
    #
    @staticmethod
    def check_constraints(nums, target):
        if 3 > len(nums) or len(nums) > 500 or -10 ** 4 > target or target > 10 ** 4:
            raise ValueError

    def find_closest(self, nums, target):
        # breakpoint()
        sorted_nums = sorted(nums.copy())
        three_sum = sorted_nums[0] + sorted_nums[1] + sorted_nums[2]
        diff_from_target = abs(three_sum - target)
        closest_sum_to_target = three_sum
        if diff_from_target == 0:
            return closest_sum_to_target

        for i, first in enumerate(sorted_nums):
            for j, second in enumerate(sorted_nums[i+1:], i+1):
                two_sum = first + second
                remaining_to_target = two_sum - target
                search_point = bisect.bisect(sorted_nums, remaining_to_target, lo=j+1)
                start_index = j+1
                end_index = len(nums)-1

        return closest_sum_to_target


class TestSolution:
    @pytest.mark.parametrize("nums, target, expected", [
        # ([-1, 2, 1, -4], 1, 2),
        ([-1, -1, 0, -1], -4, -3),
        ([0, 0, 0], 1, 0),
        # ([0, 0, 0, 6], 1, 0),
        # ([0, 0, 0, 6], 8, 6),
        # ([0, 1, 2], 0, 3),
        # ([-10, -20, -30, 40], -1000, -60),
        ([745,912,-435,435,-290,857,354,927,-768,409,-450,13,-508,589,415,-383,-903,921,-641,532,36,-614,-522,-417,631,-601,452,-846,-788,-115,264,840,820,-284,699,860,96,-453,165,-443,973,552,-228,453,478,-139,888,667,249,31,346,-915,-431,-874,-449,-471,-833,-599,-929,-295,-971,77,536,393,-43,321,404,-310,698,-657,615,-801,-973,-870,-569,953,-133,-827,451,-101,-707,72,-862,-317,633,-120,722,262,-493,204,-515,-325,-628,6,84,577,923,11,-191,636,733,379,494,867,535,-797,345,-564,673,-237,847,-368,-873,694,186,-635,364,714,-790,-719,-152,106,-679,-812,233,-253,498,-59,-868,-786,0,-146,-486,-995,470,-207,341,-690,977,-796,757,878,-90,-72,-214,-451,-106,-795,-180,403,-255,493,467,-459,623,762,-192,-271,-463,259,967,725,884,-250,610,377,763,-61,358,664,987,122,-482,-87,109,658,-366,1000,-63,-902,-96,316,-742,516,-287,-716,719,-959,-683,-787,662,-653,-779,868,635,151,-343,496,230,591,-944,-404,-448,-773,-772,-326,-76,-335,821,-839,-875,-765,-703,-91,-542,-48,876,-381,396,-520,-134,-747,444,-487,731,-596,-78,-872,256,-82,-578,601,528,894,-771,-852,400,796,-495,147,571,-849,-674,-880,-892,218,803,966,909,-142,226,370,-401,223,229,-810,741,-93,-755,399,448,629,547,-568,593,193,-603,960,-282,555,241,449,572,832,56,-584,-618,-921,158,607,-693,802,-842,-24,886,397,-362,98,-727,344,287,-378,-476,508,-838,-480,-580,979,418,-103,-332,-737,254,713,-642,-551,-649,-162,-590,950,-173,-218], -8392, -2939)

    ])
    def test_with_params(self, nums, target, expected):
        assert Solution().find_closest(nums, target) == expected

    # @pytest.mark.parametrize("nums, target, expected", [
    #     ([0, 0], 10000, ValueError),
    #     ([0, 0, 0], 1000000000, ValueError)
    #
    # ])
    # def test_exceptions(self, nums, target, expected):
    #     with pytest.raises(expected):
    #         Solution().threeSumClosest(nums, target)
