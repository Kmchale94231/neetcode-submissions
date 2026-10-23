class Solution:

    def encode(self, strs: List[str]) -> str:
        long_string = ""

        for word in strs:
            i = 0
            for char in word:
                i += 1
                
            long_string += str(i) + "#" + word
            
        return long_string


    def decode(self, s: str) -> List[str]:
        
        word_len = 0
        
        result = [] 
        
        i = 0
        
        while i < len(s):
            hash_position = s.find("#", i)
            word_len = int(s[i:hash_position])

            i = hash_position
            
            start = hash_position + 1
            end = start + word_len
            
            result.append(s[start:end])
        
            i = end
            
        return result
