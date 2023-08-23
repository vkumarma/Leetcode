class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        import copy
        if len(nums) == 1:
            return [nums]

        def permutation(nums, l, c):
            s = set()
            if len(nums) == 1:
                l[-1].append(nums[0])
                c.append(copy.copy(l[-1]))
                l[-1].pop()
                return c

            for i in range(len(nums)):
                if nums[i] not in s:
                    s.add(nums[i])
                    temp = nums[:i] + nums[i + 1:]
                    if len(l) == 0:
                        l.append([nums[i]])
                    else:
                        l[-1].append(nums[i])
                    permutation(temp, l, c)
                    l[-1].pop()
            return c
        
        return permutation(nums, [], [])
