class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}

        for str in strs:
            key = [0] * 26
            for letter in str:
                key[ord(letter) - ord('a')] += 1
            key = tuple(key)
            if key not in map:
                map[key] = []
            map[key].append(str)

        return list(map.values())
        