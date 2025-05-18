int maxArea(int* height, int heightSize) {
    int area,largest=0;
    int right=heightSize-1;
    int left=0;
    
    while(left<right){
        int width=right-left;
        int min=(height[left]>height[right])?height[right]:height[left];
        area=min*width;
        if(area >largest) largest=area;
        if(min==height[right]) right--;
        else left++;
    }
    return largest;
}