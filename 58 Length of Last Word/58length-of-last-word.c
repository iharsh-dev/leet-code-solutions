int lengthOfLastWord(char* s) {
    int b=strlen(s)-1;
    int word=0;
    while(b>=0){
        if((*(s+b)>='a' && *(s+b)<='z')||(*(s+b)>='A' && *(s+b)<='Z') ){
            word++;
            if(b==0) return word;
            else if(*(s+b-1)==' ') return word;
            b--;
        }
        else b--;
    }
    return word;
   
}