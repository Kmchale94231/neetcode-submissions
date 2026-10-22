class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        count_sorted = sorted(count, key=lambda num: count[num], reverse=True)

        return count_sorted[0:k]

