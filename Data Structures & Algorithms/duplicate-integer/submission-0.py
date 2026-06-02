class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsList = {}
        for num in nums:
            numString = str(num)
            if numsList.get(numString) is None:
                numsList[numString] = 1
            else: 
                return True
        return False
