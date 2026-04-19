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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.empty()){
            return nullptr;
        }

        // control the merging times
        while(lists.size() > 1){
             vector<ListNode*> res;
            for(int i = 0; i < lists.size(); i+=2){
                ListNode* curr_1 = lists[i];
                ListNode* curr_2 = i+1 < lists.size() ? lists[i+1] : nullptr;
                res.push_back(mergeList(curr_1, curr_2));
            }
            lists = res;
        }
        return lists[0];
    }


    ListNode* mergeList(ListNode* l1, ListNode* l2){
            ListNode dummy;
            ListNode* temp_new_list = &dummy;
            ListNode* temp_1 = l1;
            ListNode* temp_2 = l2;

            while(temp_1 && temp_2){
                if(temp_1->val < temp_2->val){
                    temp_new_list->next = temp_1;
                    temp_1 = temp_1->next;
                }else{
                    temp_new_list->next = temp_2;
                    temp_2 = temp_2->next;
                }
                temp_new_list = temp_new_list->next;
            }
            if(temp_1){
                temp_new_list->next = temp_1;
            }else{
                temp_new_list->next = temp_2;
            }
            return dummy.next;
        }
    
};
