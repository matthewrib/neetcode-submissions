class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums) # first thing to do is sort it, sorted is O(nlogn)
        result = [] # list that contains the triplets

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: # to skip the duplicate
                continue  
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return result