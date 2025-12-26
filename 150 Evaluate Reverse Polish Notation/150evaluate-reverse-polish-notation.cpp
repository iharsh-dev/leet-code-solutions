class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        vector<int> v;
        for(int i=0;i<tokens.size();i++){
            int temp;
            if(tokens[i]=="+"){
                temp=v.back()+v[v.size()-2];
                v.erase(v.end()-2,v.end());
                v.push_back(temp);
            }
            else if(tokens[i]=="-"){
                temp=v[v.size()-2]-v.back();
                v.erase(v.end()-2,v.end());
                v.push_back(temp);
            }
            else if(tokens[i]=="*"){
                temp=v.back()*v[v.size()-2];
                v.erase(v.end()-2,v.end());
                v.push_back(temp);
            }
            else if(tokens[i]=="/"){
                temp=v[v.size()-2]/v.back();
                v.erase(v.end()-2,v.end());
                v.push_back(temp);
            }
            else{
                v.push_back(stoi(tokens[i]));
            }
        }
        return v.back();
    }
};