int romanToInt(char* s) {
    int result=0,i=0;
    while(*(s+i)!='\0'){
        switch (*(s+i)) {
            case 'I' : 
            if(*(s+i+1)=='V'){
                result+=4; 
                i++;
                break;
            }
            else if(*(s+i+1)=='X'){
                result+=9; 
                i++;
                break;
            }
            else result+=1; break;
            case 'V' : result+=5; break;
            case 'X' : 
            if(*(s+i+1)=='L'){
                result+=40;
                i++;
                break;
            }
            else if(*(s+i+1)=='C'){
                result+=90;
                i++;
                break;
            }
            else result+=10; break;
            case 'L' : result+=50; break;
            case 'C' : 
            if(*(s+i+1)=='D'){
                result+=400;
                i++;
                break;
            }
            else if(*(s+i+1)=='M'){
                result+=900;
                i++;
                break;
            }
            else result+=100; break;
            case 'D' : result+=500; break;
            case 'M' : result+=1000; break;
        }
        i++;
    }
    return result;
}