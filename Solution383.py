class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        '''
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        '''
        magazine_chars = list(magazine)
        for char in ransomNote:
            if char not in magazine_chars:
                return False
            magazine_chars.remove(char)
        return True