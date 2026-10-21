class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            seen = {}

            for index, i in enumerate(nums):

                difference = target - i

                if difference in seen:
                    return [seen[difference], index]

                seen[i] = index












            

