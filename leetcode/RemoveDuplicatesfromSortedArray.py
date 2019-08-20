class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        item = 0
        index = item + 1
        
        while index <= len(nums):
            if item < len(nums) and index < len(nums):
                if nums[item] == nums[index]:
                    del nums[index]
                else:
                    item += 1
                    index = item + 1
            else:
                break
        
        return len(nums)