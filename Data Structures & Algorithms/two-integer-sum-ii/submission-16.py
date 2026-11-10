class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(numbers)):
            goal = target - numbers[i]
            if goal in map:
                return [map[goal] + 1, i + 1]
            else:
                map[numbers[i]] = i

