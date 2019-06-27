class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        List = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if nums[i]+nums[j] == target:
                    List.append(i)
                    List.append(j)
                    return List
                else:
                    continue
        return