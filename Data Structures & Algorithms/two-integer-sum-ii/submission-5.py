class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = set(numbers)
        for num in numSet:
            if target - num in numSet - {num}:
                return sorted([numbers.index(num) + 1, numbers.index(target - num) + 1])