def partition_list(self, head, x):
    frontStart = None
    frontEnd = None
    backStart = None
    backEnd = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = None
        if curr.val < x:
            if not frontStart:
                frontStart = curr
                frontEnd = frontStart
            else:
                frontEnd.next = curr
                frontEnd = curr
        else:
            if not backStart:
                backStart = curr
                backEnd = backStart
            else:
                backEnd.next = curr
                backEnd = curr
                curr = nxt

    if frontEnd:
        frontEnd.next = backStart
        return frontStart
    else:
        return backStart