class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        vector<int> x(n),y(n);
        x.insert(x.begin(),nums.begin(),nums.begin()+n+1);
        y.insert(y.begin(),nums.begin()+n,nums.end());
        vector<int> ans;
        for(int i=0;i<n;i++){
            ans.push_back(x[i]);
            ans.push_back(y[i]);
        }
        return ans;
        
    }
};