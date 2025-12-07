class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans={-1,-1};
        if(nums.size()==0) return ans;
        int i=0,j=nums.size()-1;
        while(i!=j+1){
            if(nums[(i+j)/2]==target){
                int begin=(i+j)/2,end=(i+j)/2;
                while(begin!=0 && nums[begin-1]==target){
                    begin--;
                }
                while(end!=nums.size()-1 && nums[end+1]==target){
                    end++;
                }
                ans[0]=begin;
                ans[1]=end;
                break;
            }
            else if(nums[(i+j)/2]<target){
                i=(i+j)/2+1;
            }
            else{
                j=(i+j)/2-1;
            }
        }
        return ans;
    }
};