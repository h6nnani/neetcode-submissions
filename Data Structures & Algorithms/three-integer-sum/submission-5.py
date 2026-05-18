class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        answer = []

        for i, a in enumerate(sorted_nums):
            if i > 0 and a == sorted_nums[i-1]:
                continue

            left, right = i + 1, len(sorted_nums) - 1

            while left < right:
                result = a + sorted_nums[left] + sorted_nums[right]
                if result == 0:
                    answer.append([a, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    
                    while sorted_nums[left] == sorted_nums[left - 1] and left < right:
                        left +=1
                elif result > 0:
                    right -= 1
                elif result < 0:
                    left += 1
        
        return answer