class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longestConsecutive = 1
        counter = 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                counter +=1
                longestConsecutive = max(longestConsecutive, counter)
            elif nums[i] == nums[i-1]:
                continue
            else:
                counter = 1
        
        return longestConsecutive
            
            