class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax <= rightMax:
                l += 1
                rain = leftMax - height[l]
                if rain >= 0:
                    res+= rain
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                rain = rightMax - height[r]
                if rain >= 0:
                    res+= rain
                rightMax = max(rightMax, height[r])

        return res