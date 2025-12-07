class Solution {
public:
    string convert(string s, int numRows) {
        vector < vector<char> > v(numRows,vector<char>(2*((s.size()/2)+1)));
        int i=0,j,k=0;
        while(s[i]!='\0'){
            for(j=0;j<numRows;j++){
               if(s[i]=='\0') break;
                v[j][k]=s[i];
               i++;
            }
            k++;
            for(j=numRows-2;j>0;j--){
                if(s[i]=='\0') break;
                v[j][k]=s[i];
                i++;
                k++;
            }
        }
        string ans;
        for(int i=0;i<numRows;i++){
            for(int j=0;j<2*(s.size()/2+1);j++){
                if(v[i][j]!='\0'){
                    ans.push_back(v[i][j]);
                }
            }
        }
        return ans;
    }
};