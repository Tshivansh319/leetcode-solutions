class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        n=len(nums)
        for i in range(n):
            sum=-1*nums[i]
            if(i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while(left<right):
                s = nums[left]+nums[right]
                if(s==sum):
                    result.append([nums[i],nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while(left<n and nums[left]==nums[left-1]):
                        left=left+1
                    while(right>=0 and nums[right]==nums[right+1]):
                        right=right-1
                elif (s<sum):
                    left=left+1
                else :
                    right=right-1
        return result

