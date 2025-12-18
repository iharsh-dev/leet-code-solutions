class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        vector<int> hash(nums.size()+1,0);
        vector<int> ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++){
            if(hash[nums[i]]==0){
                hash[nums[i]]=nums[i];
            }
            else{
                ans.push_back(nums[i]);
            }
        }
        for(int i=1;i<hash.size();i++){
            if(hash[i]==0){
                ans.push_back(i);
                break;
            }
        }
        return ans;
    }
};