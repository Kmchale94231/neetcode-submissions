class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_sub = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])           
            
            curr_sub = r - l + 1
            
            max_sub = max(max_sub, curr_sub)
        return max_sub
                
            
