class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> heap(nums.size()+1,0);
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            heap[nums[i]]=nums[i];
        }
        for(int i=1;i<=nums.size();i++){
            if(heap[i]==0){
                ans.push_back(i);
            }
        }
        return ans; 
    }
};