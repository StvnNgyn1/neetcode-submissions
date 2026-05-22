class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1, count_s2 = Counter(s1), Counter(s2[:len(s1)])
        
        matches = 0
        for letter in count_s1:
            matches += (1 if count_s1[letter] == count_s2[letter] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == len(count_s1):
                return True

            char = s2[r]
            count_s2[char] += 1
            if char in count_s1:
                if count_s1[char] == count_s2[char]:
                    matches += 1
                elif count_s1[char] + 1 == count_s2[char]:
                    matches -= 1

            char = s2[l]
            count_s2[char] -= 1
            if char in count_s1:
                if count_s1[char] == count_s2[char]:
                    matches += 1
                elif count_s1[char] - 1 == count_s2[char]:
                    matches -= 1
            l += 1
        return matches == len(count_s1)