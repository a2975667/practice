class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dictionary = {}
        
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = i
            else:
                if i - dictionary[nums[i]] <= k:
                    return True
                else:
                    dictionary[nums[i]] = i
        return False
                