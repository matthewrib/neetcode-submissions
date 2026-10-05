class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = 1
        rightProduct = 1
        productList = []
        for i in range(len(nums)):
            productList.append(1)
        for i in range(len(nums)):
            productList[i] = leftProduct
            leftProduct *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            productList[i] *= rightProduct
            rightProduct *= nums[i]
        return productList
