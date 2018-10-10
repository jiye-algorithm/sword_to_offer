'''
通过 x将链表分为两部分，前面部分小于x， 后面部门大于等于x

在两个链表中保持元素的相对位置

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
Contributor

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        curr = head
        beforeStart = None
        beforeEnd = None
        afterStart = None
        afterEnd = None
        
        while curr:
            # we need to save whatever current is pointing to because we will be adding current to
            # the end of one of two lists, which means we have to ensure curr points to NULL
            next = curr.next
            
            # this is the setup to make curr eligible to become the end-node of the before or after linked list
            curr.next = None
    
            if curr.val < x:
                # if the value is less than x and the list is empty
                if beforeStart == None:
                    beforeStart = curr
                    beforeEnd = beforeStart
                # if list isn't empty, connect the current node to the end of the "before" list
                else:
                    beforeEnd.next = curr
                    beforeEnd = curr
            else:
                # if the value is equal or greater than x and the list is empty
                if afterStart == None:
                    afterStart = curr
                    afterEnd = afterStart
                # if the "after" list already has nodes, just connect the current node to its end
                else:
                    afterEnd.next = curr
                    afterEnd = curr
            # increment for next while loop iteration
            curr = next
        
        # if there is nothing before, then return only the 2nd list
        if beforeStart == None:
            return afterStart
        
        # connect the 2 lists together
        beforeEnd.next = afterStart
        
        # submit with the new head
        return beforeStart
        
        