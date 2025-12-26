class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int b=0;
        for(int i=1;i<=n;i++){
            if(b+1>target.size()) break;
            if(i==target[b]){
                ans.push_back("Push");
                b++;
            }
            else{
                ans.push_back("Push");
                ans.push_back("Pop");
            }
        }
        return ans;
    }
};