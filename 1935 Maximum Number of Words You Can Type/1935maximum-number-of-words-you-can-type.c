int canBeTypedWords(char* text, char* brokenLetters) {
    int i=0;
    int ans=0;
    while(text[i]!='\0'){
        int check=0;
        while(text[i]!=' ' && text[i]!='\0'){
            int j=0;
            while(*(brokenLetters+j)!='\0'){
                if(text[i]==*(brokenLetters+j)){
                    check++;
                }
                j++;
            }
            i++;
        }
        if(!check) ans++;
        if(text[i]=='\0') continue;
        else i++;
    }
    return ans;
}