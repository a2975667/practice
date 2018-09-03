class Solution:
    def containsDuplicate(self, nums):
        entry = {}
        if len(nums) < 2:
            return False
        for x in nums:
            if x not in entry:
                entry[x] = 1
            else:
                return True
        return False