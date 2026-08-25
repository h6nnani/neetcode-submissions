class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # value : index, has the previous visited numbers in nums

        for i, val in enumerate(nums): # enumerate lists out index and value respectfully
            difference = target - val
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[val] = i # visited that value in index i, add to hashmap
        
        return [0,0] # if no solution is found
