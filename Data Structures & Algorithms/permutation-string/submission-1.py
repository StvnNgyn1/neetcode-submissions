class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = defaultdict(int)
        for c in s1:
            count_s1[c] += 1
        print(count_s1)
        

        l = 0

        for r in range(len(s1), len(s2) + 1):
            count_s2 = defaultdict(int)
            for i in range(l, r):
                count_s2[s2[i]] += 1
            print(count_s2)
            if count_s1 == count_s2:
                return True
            else:
                count_s2[s2[l]] -= 1
                l += 1
        return False

