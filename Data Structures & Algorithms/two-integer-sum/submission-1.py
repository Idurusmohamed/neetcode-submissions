class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #maps value -> index

        for i, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement],i]
            seen[number] = i
            


