# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Iteration method (time: O(n*k), space: O(1))
        
        res = ListNode(0)  # Dummy node serving as fixed start of merged list
        cur = res          # Pointer tracking the tail of our growing merged list

        while True:
            minNode = -1   # Reset every round: -1 means no valid node picked yet
            
            for i in range(len(lists)):
                if not lists[i]:
                    continue  # Skip empty or fully traversed lists
                
                # Pick list `i` if it's the 1st valid candidate or has a smaller value
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
                
            if minNode == -1:
                break  # Exit loop when all lists are completely empty
            
            cur.next = lists[minNode]             # STITCH: Link smallest node to result list
            lists[minNode] = lists[minNode].next  # ADVANCE LIST: Shift picked list's head forward
            cur = cur.next                        # ADVANCE RESULT: Move `cur` to the new tail
            
        return res.next  # Return merged list head, skipping dummy node (0)