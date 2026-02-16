class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)   
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

           
            if l1:
                v1 = l1.val
            else:
                v1 = 0

           
            if l2:
                v2 = l2.val
            else:
                v2 = 0

            total = v1 + v2 + carry

            carry = total // 10      
            digit = total % 10       

            curr.next = ListNode(digit)
            curr = curr.next

            
            if l1:
                l1 = l1.next

           
            if l2:
                l2 = l2.next

        return dummy.next
