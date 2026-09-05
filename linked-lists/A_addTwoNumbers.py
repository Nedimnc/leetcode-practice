"""
Problem: [Problem Name]
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: Medium
Pattern: Linked List 

Approach:
- We treat this like basic addition, where we add the digits from the two linked lists and keep track of any carry.
- Since digits are stored in reverse order, we can start from the head of both lists and move forward.
- Iterate while either list still has nodes OR there's a carry to process.
- Create a new node with (sum % 10) and update carry to (sum // 10).
- Continue until both lists are fully traversed and there's no carry left.

Time Complexity: O(max(m, n)) -> We loop through the length of the longer linked list.
Space Complexity: O(max(m, n)) -> The new linked list has at most max(m, n) + 1 nodes.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)     #our fake starting node to handle the result list
        curr = dummy            #pointer to track the tail 
        carry = 0               #keeps track of any digit carried over (0 or 1)

        #we want to keep looping if l1 has nodes, l2 has nodes, OR there's a leftover carry to append
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0 #grab the digit from l1, or 0 if l1 has run out
            val2 = l2.val if l2 else 0 #grab the digit from l2, or 0 if l2 has run out

            total = val1 + val2 + carry #add both diigts plus w/e carried over
            carry = total // 10         #compute new carry (ex. 14 // 10 = 1)
            digit = total % 10          #compute the single digit to store (ex. 14 // 10 = 4)

            curr.next = ListNode(digit) #create and attach the new node with our digit
            curr = curr.next            #advance our result list pointer

            #move forward in l1 and l2 ONLY if they still have nodes remaining
            if l1:
                l1 = l1.next
            if l2: 
                l2 = l2.next

        return dummy.next   #dummy.next just skips the fake starting node and returns the actual head
        