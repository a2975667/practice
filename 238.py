class Solution:
    def productExceptSelf(self, nums):
        asc = []
        dsc = []
        dsc = [1]*len(nums)
        s = 1
        for i in range(len(nums)):
            asc.append(s)
            s = s * nums[i]
        s = 1
        for i in range(len(nums))[::-1]:
            dsc[i] = s
            s = s * nums[i]
        # print (asc)
        # print (dsc)
        
        final = []

        for i in range(len(nums)):
            final.append(asc[i] * dsc[i])
        return final
                                   
