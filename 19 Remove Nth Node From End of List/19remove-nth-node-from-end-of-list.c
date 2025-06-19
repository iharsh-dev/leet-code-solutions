/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *t,*prev,*ans=NULL,*h;
    int count=0,c=0;
    t=head;
    h=head;
    while(t!=NULL){
        count++;
        t=t->next;
    }
    if(count==1) return ans;
    if(count==n){
        head=head->next;
        return head;
    }
    count=count-n;
    while(head!=NULL){
        if(c==count){
            prev->next=head->next;
            head->next=NULL;
            return h;
        }
        prev=head;
        c++;
        head=head->next;
    }
    return head;

}