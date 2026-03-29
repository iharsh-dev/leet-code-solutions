class Solution {
public:
    int reverse(int x) {
        long long a=x;
        long long poww=pow(2,31);
        int check=0;
        if(a>0){
            check=1;
        }
        else{
            check=-1;
        }
        a=a*check;
        long long reverse=0;
        while (a>0){
            reverse*=10;
            reverse+=a%10;
            a=a/10;
        }
        if(reverse>= poww-1 || reverse <= -poww){
            return 0;
        }
        else{
            return check*reverse;
        }

    }
};