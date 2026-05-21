class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tracker = {}
        maxLength = 0

        l = 0
        for r in range(len(s)):
            if s[r] in tracker:
                l = max(tracker[s[r]] + 1, l)
            tracker[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
        return maxLength