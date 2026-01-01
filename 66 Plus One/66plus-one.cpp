class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int count=0;
        vector<int> ans=digits;
        for(int i=0;i<digits.size();i++){
            if(digits[i]==9){
                count++;
            }
        }
        if(count==digits.size()){
            fill(ans.begin(),ans.end(),0);
            ans.push_back(0);
            ans[0]=1;
        }
        else if(digits.back()==9){
            int i=digits.size()-1;
            while(i>=0 && ans[i]==9){
                ans[i--]=0;
            }
            ans[i]+=1;
        }
        else{
            ans[digits.size()-1]+=1;
        }
        return ans;
    }
};