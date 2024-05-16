import copy
from typing import List


class Permutations:

    def permute(self, nums: List[int]) -> List[List[int]]:
        result_list: List[List[int]] = []
        temp_list: List[int] = []
        self._back_tracking(nums, result_list, temp_list)
        return result_list

    def _back_tracking(self, nums: List[int], result_list: List[List[int]], temp_list: List[int]):
        if temp_list.__len__() == nums.__len__():
            result_list.append(copy.deepcopy(temp_list))
        else:
            for num in nums:
                if num in temp_list:
                    continue
                temp_list.append(num)
                self._back_tracking(nums, result_list, temp_list)
                temp_list.remove(num)


if __name__ == "__main__":
    permutations: Permutations = Permutations()
    print(permutations.permute([1, 2, 3]))
