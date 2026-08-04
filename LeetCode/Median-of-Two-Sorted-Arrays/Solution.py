1double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
2    int i=0,j=0,k=0;
3    int num=nums1Size+nums2Size;
4    double arr[num];
5    while(i<nums1Size && j<nums2Size){
6       if(*(nums1+i)<*(nums2+j)){
7        arr[k++]=*(nums1+i++);
8       }
9       else{
10        arr[k++]=*(nums2+j++);
11       }
12    }
13    while(j<nums2Size){
14        arr[k++]=*(nums2+j++);
15    }
16    while(i<nums1Size){
17        arr[k++]=*(nums1+i++);
18    }
19    if(num%2!=0){
20        return arr[(num)/2];
21    }
22    else{
23        return (arr[(num)/2]+arr[(num)/2-1])/2.0;
24    }
25}