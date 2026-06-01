class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l = 0
        freq = {}
        window_map = {}
        min_len = float('inf') 
        result_indices = [-1, -1]
        
        
        for right in range(len(t)):
            if t[right] in freq:
                freq[t[right]] += 1
            else:
                freq[t[right]] = 1
                
        need = len(freq)
        have = 0
        
        for right in range(len(s)):
            if s[right] in window_map:
                window_map[s[right]] += 1
            else:
                window_map[s[right]] = 1
            
            if s[right] in freq:
                if window_map[s[right]] == freq[s[right]]:
                    have +=1
            
            while have == need:
                if (right - l + 1) < min_len:
                    min_len = right - l + 1
                    result_indices = [l, right]
                
                if s[l] in freq:
                    window_map[s[l]] -= 1
                    
                    if window_map[s[l]] < freq[s[l]]:
                        have -= 1
                        
                l += 1
        start, end = result_indices
        return s[start : end + 1] if min_len != float('inf') else "" 