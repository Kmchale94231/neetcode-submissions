class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word: 
                index = alphabet.index(char)

                count[index] += 1
            
            key = tuple(count)

            if key in groups: 
                groups[key].append(word)
            
            else:
                groups[key] = [word]
        
        return list(groups.values())











        