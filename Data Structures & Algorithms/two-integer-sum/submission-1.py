class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in memory:
                return sorted([i, memory.get(difference)])
            else:
                memory[nums[i]] = i
