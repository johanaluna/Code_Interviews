def shiftLinkedList(head, k):
    # Write your code here.
	def backward(head , p1, p2):
		while p1.next:
			p1 = p1.next
			p2 = p2.next

		p3 = p2.next
		p2.next = None
		p1.next = head
		head = p3
		return head
	
	
	def forward(head , p1, p2):
		p3 = p1
		while p2.next != p1:
			p2 = p2.next
		
		while p3.next:
			p3 = p3.next
			
		p2.next = None
		p3.next = head
		head = p1
		return head			
		
    if head is None or k is 0:
		return head

	p2 = p1 = head
	counter = abs(k)
	
	while counter != 0:
		if p1.next == None:
			p1 = head
		else:
			p1 = p1.next
		counter -= 1
		
	if p1 is head:
		return head
	
	elif k > 0:
		return backward(head , p1, p2)
	
	else:
		return forward(head , p1, p2)
		
		
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
    