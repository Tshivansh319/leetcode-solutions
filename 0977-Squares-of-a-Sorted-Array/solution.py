class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        for item in nums:
            if item<0:
                neg.append(item*item)
            else:
                pos.append(item*item)
        neg=neg[::-1]
        n=len(pos)
        m=len(neg)
        result=[]
        i=0;j=0;id=0
        while i<n and j<m:
            if pos[i]<neg[j]:
                result.append(pos[i])
                i=i+1
            else:
                result.append(neg[j])
                j=j+1
        while i<n:
            result.append(pos[i])
            i=i+1
        while j<m:
            result.append(neg[j])
            j=j+1

        return result
