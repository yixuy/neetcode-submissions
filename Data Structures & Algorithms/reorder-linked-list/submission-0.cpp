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
        if(head == nullptr){
            return;
        }
        vector<ListNode*> nodeList;
        ListNode* curr = head;
        while(curr){
            nodeList.push_back(curr);
            curr = curr->next;
        }
        ListNode* res = head;
        for(int i = 0; i < (nodeList.size()+1)/2; i++){
            res->next = nodeList[i];
            res = res->next;
            res->next = nodeList[nodeList.size() - 1  - i];
            res = res->next;
        }
        // make the last element in linkedlist nullptr 
        res->next = nullptr;
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
    }
};
