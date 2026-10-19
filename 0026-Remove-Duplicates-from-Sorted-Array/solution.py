class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n=len(nums)
        start=0
        if n==0:
            return 0

        for i in range(1,n):
            if nums[start]!=nums[i]:
                start+=1
                nums[start]=nums[i]

        return start+1
        