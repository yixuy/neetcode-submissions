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
    void reorderList(ListNode* head) {
        // if(head == nullptr){
        //     return;
        // }
        // vector<ListNode*> nodeList;
        // ListNode* curr = head;
        // while(curr){
        //     nodeList.push_back(curr);
        //     curr = curr->next;
        // }
        // ListNode* res = head;
        // for(int i = 0; i < (nodeList.size()+1)/2; i++){
        //     res->next = nodeList[i];
        //     res = res->next;
        //     res->next = nodeList[nodeList.size() - 1  - i];
        //     res = res->next;
        // }
        // // make the last element in linkedlist nullptr 
        // res->next = nullptr;
        // int i = 0;
        // int j = nodeList.size()-1;
        // while (i < j){
        //     nodeList[i++]->next = nodeList[j];
        //     if(i >= j){
        //         break;
        //     }
        //     nodeList[j--]->next = nodeList[i];
        // }
        // nodeList[i]->next = nullptr;

        
        // use slow pointer and fast pointer to get the middle
        ListNode* slow = head;
        ListNode* fast = head;

        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        // reverse the second part
        ListNode* second = slow->next;
        slow->next = nullptr;
        ListNode* curr = second;
        ListNode* prev = nullptr;

        while(curr){
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }
        second = prev;
        ListNode* first = head;
        // merge to one list 
        while(second){
            ListNode* temp1 = first->next;
            ListNode* temp2 = second->next;
            first->next = second;
            second->next = temp1;
            first = temp1;
            second = temp2;
        }
        // reverse the 
    }
};
