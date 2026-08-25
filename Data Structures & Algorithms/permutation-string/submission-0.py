class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_dict = {}

        s2_dict = {}

        for letter in s1:
            s1_dict[letter] = 1 + s1_dict.get(letter, 0)
        for letter in s2:
            s2_dict[letter] = 1 + s2_dict.get(letter,0)

        print(s1_dict)
        print(s2_dict)
        for entry in s1_dict.keys():
            if not s2_dict[entry]:
                return False
            elif s1_dict[entry] != s2_dict[entry]:
                return False
            
                
        return True