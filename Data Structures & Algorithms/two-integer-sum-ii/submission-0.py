class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # first = numbers[0]
        # for x in numbers:
        #     remainder = target - first
        #     if x == remainder and numbers.index(first) != numbers.index(remainder):
        #         return [first, remainder]
        #     else:
        #         first = x

        first = 0
        last = len(numbers) - 1

        for x in range(len(numbers)):
            result = numbers[first] + numbers[last]
            if result == target and first < last:
                return [first + 1, last + 1]
            elif result < target:
                first += 1
            elif result > target:
                last -= 1

        return [0,0]
