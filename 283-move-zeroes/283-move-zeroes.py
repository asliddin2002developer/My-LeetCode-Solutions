class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Time Complexty: O(n)
        # Space Complexity: O(n)
        # i = 0
        # for _ in range(len(nums)):
        #     if nums[i] == 0:
        #         zero = nums.pop(i)
        #         nums.append(zero)
        #     else:
        #         i += 1
        
        
        # Time Complexty: O(n)
        # Space Complexity: O(1)
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i]= nums[i], nums[k]
                k += 1
            