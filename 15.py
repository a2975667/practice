class Solution:    
    def threeSum(self, nums):
        
        # Special Case Handleing
        if len(nums) < 3:
            return []
        
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        
        #Sorting
        nums.sort()
        result = []
        
        # O(n)
        for i in range(len(nums)-2):
            
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            left_ptr = i+1
            right_ptr = len(nums)-1
            
            # O(n)
            while left_ptr < right_ptr:
                
                s = nums[i] + nums[left_ptr] + nums[right_ptr]
                if s == 0:
                    result.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr-1]:
                        left_ptr += 1
                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr+1]:
                        right_ptr -= 1
                
                elif s > 0:
                    right_ptr -= 1
                else:
                    left_ptr += 1
        
        return result
                    