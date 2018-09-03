class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        counter = 0
        for num in nums:
            if num is not 0:
                nums[ptr] = num
                ptr += 1
                counter += 1
        for x in range(counter, len(nums)):
            nums[x] = 0
            
                
                