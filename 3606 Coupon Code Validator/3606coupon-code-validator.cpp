class Solution {
public:
    vector<string> validateCoupons(vector<string>& code, vector<string>& businessLine, vector<bool>& isActive) {
        vector <bool> v(code.size(),true);
        vector<int> s;
        for(int i=0;i<code.size();i++){
            if(businessLine[i]!="electronics" && businessLine[i]!="grocery" && businessLine[i]!="pharmacy" && businessLine[i]!="restaurant"){
                v[i]=false;
                continue;
            }
            if(!isActive[i]){
                v[i]=false;
                continue;
            }
            if(code[i].size()==0){
                v[i]=false;
                continue;
            }
            for(int j=0;j<code[i].size();j++){
                if(!isalnum((unsigned char)code[i][j]) && code[i][j]!='_' ){ 
                    v[i]=false;
                    break;
                }
            }
        }
        for(int i=0;i<v.size();i++){
            if(v[i]){
                s.push_back(i);
            }
        }
        vector< vector<string> > a(4);
        for(int i=0;i<s.size();i++){
            if(businessLine[s[i]]=="electronics"){
                a[0].push_back(code[s[i]]);
            }
            else if(businessLine[s[i]]=="grocery"){
                a[1].push_back(code[s[i]]);
            }
            else if(businessLine[s[i]]=="pharmacy"){
                a[2].push_back(code[s[i]]);
            }
            else{
                a[3].push_back(code[s[i]]);
            }
        }
        for(int i=0;i<4;i++){
            sort(a[i].begin(),a[i].end());
        }
        vector<string> ans;
        for(int b=0;b<a.size();b++){
            for(int c=0;c<a[b].size();c++){
                ans.push_back(a[b][c]);
            }        
        }
        return ans;
    }
};