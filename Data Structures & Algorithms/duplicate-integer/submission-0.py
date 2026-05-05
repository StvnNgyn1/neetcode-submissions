class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for number in range(1, len(nums)):
            if nums[number] == nums[number -1]:
                return True
        return False