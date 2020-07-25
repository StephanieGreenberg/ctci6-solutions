def getLen(head):
    len = 0
    while head:
        len+=1
        head = head.next
    return len

def intersection(self, l1, l2):
	if l1 is None or l2 is None:
		return None

	l1Count = getLen(l1)
	l2Count = getLen(l2)

	smaller = l1 if l1Count < l2Count else l2
	larger = l2 if l1Count < l2Count else l1

	countDiff = abs(l1Count - l2Count)

	for _ in range(countDiff):
		larger = larger.next

	while larger:
		if smaller == larger:
			return smaller
        smaller = smaller.next
        larger = larger.next
    return None

