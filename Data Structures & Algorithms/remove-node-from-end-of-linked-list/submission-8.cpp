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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        // calculate the index using len(list)
        ListNode* temp = head;
        int count = 1;
        while(temp->next){
            temp = temp->next;
            count++;
        }

        // int index = n % count;
//  [1,2,3,4, 5], n = 2
        
        ListNode* remove = head;
        for(int i = 0; i < count - n - 1; i++){
            remove = remove->next;
        }

        if(remove == head && count - n != 1){
            head = head->next;
        }else{
            remove->next = remove->next->next;
        }
        return head;
    }
};
