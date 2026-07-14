class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        max_length = 0

        for i in nums:
            if i-1 in unique_nums:
                continue
            current_length = 1
            current_element = i+1
            while current_element in unique_nums:
                current_length+=1
                current_element+=1
            
            max_length = max(max_length, current_length)

        return max_length

        
