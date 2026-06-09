class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash = {}
        ans = []

        length = len(nums) / 3

        for num in nums:
            hash[num] = hash.get(num, 0 ) + 1
        
        for key, value in hash.items():
            if value > length:
                ans.append(key)
        return ans