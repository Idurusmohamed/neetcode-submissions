class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_consec = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in store:
                streak += 1
                curr += 1
            longest_consec = max(longest_consec, streak)
        return longest_consec
    