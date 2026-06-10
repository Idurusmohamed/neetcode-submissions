class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_length = len(nums)
        res = [1] * num_length

        prefix = 1
        for i in range(num_length):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(num_length -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res