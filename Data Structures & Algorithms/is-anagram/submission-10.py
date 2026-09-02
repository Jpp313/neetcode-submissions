class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): # two strings with diff lengths can never be anagrams
            return False

        count = [0] * 26 # 26 letters of alphabet since we are bounded to just lower chars

        for i in range(s): # loop will change freqeuencys up and down if chars are same end result should be 0 in all places meaning every char got added and deleted and none were left behind meaning one string had a diff freq of char than the other
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1

        
        for val in count:
            if val != 0:
                return False
        return True