class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        pivot_index = 0


        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r] :
                l = mid + 1 
            elif nums[mid] < nums[r]:
                r = mid
        
        pivot_index = r
        l = 0
        r = len(nums) - 1
        
        if target >= nums[pivot_index] and target <= nums[r]:
            l = pivot_index
        else:
            r = pivot_index - 1
            
        
        while l <= r:
            mid = (l + r)   // 2
            
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            elif nums[mid] == target:
                return mid
                
            
        return -1


        