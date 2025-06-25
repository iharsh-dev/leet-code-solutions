/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *first,*t,*tail;
    first=(struct ListNode*)malloc(sizeof(struct ListNode));
    first->next=NULL;
    tail=first;
    int carry=0;
    while(l1!=NULL || l2!=NULL){
        t=(struct ListNode *)malloc(sizeof(struct ListNode));
        int sum=carry;
        if(l1!=NULL){
            sum=sum+l1->val;
            l1=l1->next;
        }
        if(l2!=NULL){
            sum=sum+l2->val;
            l2=l2->next;
        }
        carry=sum/10;
        sum=sum%10;
        t->val=sum;
        t->next=NULL;
        tail->next=t;
        tail=t;
    }
    if(carry){
        t=(struct ListNode*)malloc(sizeof(struct ListNode));
        t->val=carry;
        t->next=NULL;
        tail->next=t;
        tail=t;
   }
    struct ListNode *result=(struct ListNode *)malloc(sizeof(struct ListNode));
    result=first->next;
    free(first);
    return result;

}