class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_freq = 0
        max_len = 0
        left = 0
        
        for right in range(len(s)):
            
            if s[right] in freq_map:
                freq_map[s[right]] += 1
            else:
                freq_map[s[right]] = 1
            
            max_freq = max(max_freq, freq_map[s[right]])
                
            while (right - left + 1) - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        
        return max_len