struct stack{
    int size;
    int top;
    char *p;
};
bool isValid(char* s) {
    struct stack *st;
    st=(struct stack *)malloc(sizeof(struct stack));
    st->size=strlen(s);
    st->top=-1;
    st->p=(char*)malloc(st->size*sizeof(char));
    int i=0;
    while(*(s+i)!='\0'){
        if(*(s+i)=='('||*(s+i)=='['||*(s+i)=='{'){
            st->p[++st->top]=*(s+i);
            
        }
        else if(st->top!=-1){
        if((*(s+i)==')'&& st->p[st->top]=='(') || (*(s+i)==']'&& st->p[st->top]=='[') || (*(s+i)=='}'&& st->p[st->top]=='{')){
            st->p[st->top--]='\0';
        }
        else{
            return false;
        }
        }
        else{
            return false;
        }
        i++;
    }
    if(st->top==-1) return true;
    else return false;
}