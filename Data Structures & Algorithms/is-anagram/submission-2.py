class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_ht = {}
        t_ht = {}
        
        for letter in s:
            if letter in s_ht:
                s_ht[letter] = s_ht.get(letter) + 1
            else:
                s_ht[letter] = 1
        
        for letter in t:
            if letter in t_ht:
                t_ht[letter] = t_ht.get(letter) + 1
            else:
                t_ht[letter] = 1
        
        if s_ht == t_ht:
            return True
        return False

        