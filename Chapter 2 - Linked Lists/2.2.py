def kth_to_last(head, k):
	ctr = findLength(head) - 1
	while head:
		if k == ctr:
			return head
		ctr -= 1
		head = head.next
	return None

def findLength(head):
	ctr = 0
	while head:
		ctr += 1
		head = head.next
	return ctr