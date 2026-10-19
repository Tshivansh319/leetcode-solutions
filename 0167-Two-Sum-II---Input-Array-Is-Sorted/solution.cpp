class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i=0;
        int n=numbers.size();
        int j=n-1;
        int pairSum=0;
        while(i<j){
            pairSum=numbers[i]+numbers[j];
            if(pairSum<target)
                i++;
            if(pairSum>target)
                j--;
            if(pairSum==target)
                return {i+1,j+1};
        }
        return {i+1,j+1};
    }
};
