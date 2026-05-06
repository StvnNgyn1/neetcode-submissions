class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        result = []
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            tracker[num] += 1
        
        sorted_values = sorted(tracker.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sorted_values[i][0])

        return result
