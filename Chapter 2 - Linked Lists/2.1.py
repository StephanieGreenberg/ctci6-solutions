def remove_dups(head):
	dups = {}
	curr = head

	while curr:
		if curr.val in dups:
			curr.next = curr.next.next
		else:
			dups[curr.val] = 1
	return head

def remove_dups_followup(head):
	p1 = head
	while p1:
		p2 = p1
		while p2.next:
			if p2.next.val == p1.val:
				p2.next = p2.next.next
			else:
				p2 = p2.next
			p1 = p1.next
	return head