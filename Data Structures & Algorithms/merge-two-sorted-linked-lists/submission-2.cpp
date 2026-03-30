/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* dummy = new ListNode();
        ListNode* current = new ListNode();
        current = dummy;
        ListNode* l1_head =list1;
        ListNode* l2_head =list2;
        while (l1_head !=nullptr && l2_head !=nullptr){
            if(l1_head->val<=l2_head->val){
                current->next = l1_head;
                current = current->next;
                l1_head = l1_head->next;
            }
            else{
                current->next = l2_head;
                current = current->next;
                l2_head = l2_head->next;
            }
        }
        if(l1_head == NULL){
            current->next =l2_head;
        }
        else{
            current->next = l1_head;
        }
        return dummy->next; 
        
    }
};
