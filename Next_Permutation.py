class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        l = len(nums) - 2
        r = len(nums) - 1
        if nums[l] < nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            return
        
        while l >= 0:
            if nums[l] < nums[r]:
                while r < len(nums):
                    if nums[r] <= nums[l]:
                        break
                    r += 1
                
                r -= 1
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                t = len(nums) - 1
                

                while l <= t:
                    nums[l], nums[t] = nums[t], nums[l]
                    l += 1
                    t -= 1
                    
                return 
        
            l -= 1
            r -= 1
        
        i = 0
        while i < (len(nums) // 2):
            nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            i += 1

        


