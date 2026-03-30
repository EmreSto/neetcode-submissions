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
    bool hasCycle(ListNode* head) {
        ListNode* s_start = head;
        set<ListNode*>new_set = {};
        while (s_start != nullptr){
            new_set.insert(s_start);
            if(new_set.count(s_start->next)){
                return true;
            }
            s_start = s_start->next;
        }
        return false;

        
    }
};
