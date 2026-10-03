class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums) # first thing to do is sort it, sorted is O(nlogn)
        result = [] # list that contains the triplets

        left = 0 # pointer for left
        right = 1 # pointer to check values that possibly equal to left

        while left < right: # can we possibly do a 2 sum for each left number?
            additions = {} # to find values that would possibly work
            right = left + 1
            while right < len(nums): # iterate through all numbers right of left
                if -1 * (nums[left] + nums[right]) in additions.keys():
                    additionIndex = additions[-1 * (nums[left] + nums[right])]
                    tempResult = [nums[left], nums[right], nums[additionIndex]]
                    result.append(tempResult)
                else:
                    additions[nums[right]] = right
                right += 1
            left += 1

        newResult = []
        for item in result: 
            if item not in newResult:
                newResult.append(item)

        return newResult