class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum=float('-inf')
        max_diff=float('inf')
        n=len(nums)
        nums.sort()
        for i in range(n):
            sum=target-nums[i]
            if (i>0 and nums[i]==nums[i-1]):
                continue
            left=i+1
            right=n-1
            while(left<right):
                s=nums[left]+nums[right]
                if s==sum:
                    return nums[i]+nums[left]+nums[right]
                elif s<sum:
                    diff=abs(s-sum)
                    if diff<max_diff:
                        max_diff=diff
                        result=nums[i]+nums[left]+nums[right]
                    left=left+1
                elif s>sum:
                    diff=abs(s-sum)
                    if diff<max_diff:
                        max_diff=diff
                        result=nums[i]+nums[left]+nums[right]
                    right=right-1

        return result