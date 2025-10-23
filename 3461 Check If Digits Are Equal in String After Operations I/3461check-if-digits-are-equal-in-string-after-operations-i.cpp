class Solution {
public:
    bool hasSameDigits(string s) {
        while(s.size()>2){
            string temp="";
            int i=0;
            while(s[i]!='\0' && s[i+1]!='\0'){
                int sum=(s[i]+s[i+1]-2*'0');
                temp+=sum%10+'0';
                i++;
            }
            s=temp;
        }
        if(s[0]==s[1]){
            return true;
        }
        else{
            return false;
        }
        
    }
};