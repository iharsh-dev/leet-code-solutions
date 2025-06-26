double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int i=0,j=0,k=0;
    int num=nums1Size+nums2Size;
    double arr[num];
    while(i<nums1Size && j<nums2Size){
       if(*(nums1+i)<*(nums2+j)){
        arr[k++]=*(nums1+i++);
       }
       else{
        arr[k++]=*(nums2+j++);
       }
    }
    while(j<nums2Size){
        arr[k++]=*(nums2+j++);
    }
    while(i<nums1Size){
        arr[k++]=*(nums1+i++);
    }
    if(num%2!=0){
        return arr[(num)/2];
    }
    else{
        return (arr[(num)/2]+arr[(num)/2-1])/2.0;
    }
}