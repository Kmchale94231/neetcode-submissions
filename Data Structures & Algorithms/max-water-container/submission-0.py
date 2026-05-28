class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        curr_vol = 0
        distance = 0
        max_vol = 0

        while l < r:
            curr_vol = (r - l) * min(heights[r], heights[l])
            
            if heights[l] > heights[r]:
                r -= 1
            
            elif heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            max_vol = max(curr_vol, max_vol)

        return max_vol
                

            
