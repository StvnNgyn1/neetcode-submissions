class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        tracker = set()

        currLength = 0
        l, r = 0, 0

        while r < len(s):
            
            if s[r] in tracker:
                while s[r] in tracker:
                    tracker.remove(s[l])
                    l += 1
                    currLength -= 1
            else:
                tracker.add(s[r])
                currLength += 1
                maxLength = max(maxLength, currLength)
                r += 1
        
        return maxLength
