int numTrees(int n) {
    if(n==0 || n==1) return 1;
    else{
        long double res=1;
        for(float k=2;k<=n;k++){
            res=res*(n+k)/k;
        }
        return res;
    }
}