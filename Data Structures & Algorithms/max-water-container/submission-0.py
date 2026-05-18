class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        maximum = 0

        while left < right:
            width = right - left
            maximum = max(maximum, width * min(heights[left], heights[right]))
            
            if heights[left] < heights[right]:
                left += 1  
            else:
                right -= 1
        
        return maximum