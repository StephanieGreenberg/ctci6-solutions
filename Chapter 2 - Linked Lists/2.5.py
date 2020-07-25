def addTwoNumbers(self, l1, l2):
    result = dummy = ListNode(-1)
    carry = 0
    
    while l1 or l2 or carry:
        temp1 = l1.val if l1 else 0
        temp2 = l2.val if l2 else 0
        tempSum = temp1 + temp2 + carry
        
        result.next = ListNode(tempSum % 10)
        carry = tempSum // 10

        result = result.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
     
    if l1:
        result.next = l1
    if l2:
        result.next = l2
    
    return dummy.next