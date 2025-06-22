/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *first,*current,*tail;
    first=(struct ListNode*)malloc(sizeof(struct ListNode));
    first->next=NULL;
    tail=first;
    while(list1!=NULL && list2!=NULL){
        current=(struct ListNode*)malloc(sizeof(struct ListNode));
        current->next=NULL;
        if(list1->val>=list2->val){
            current->val=list2->val;
            list2=list2->next;
        }
        else{
            current->val=list1->val;
            list1=list1->next;
        }
        tail->next=current;
        tail=current;

    }
    if(list1!=NULL) tail->next=list1;
    else tail->next=list2;
    struct ListNode *result=first->next;
    free(first);
    return result;

}