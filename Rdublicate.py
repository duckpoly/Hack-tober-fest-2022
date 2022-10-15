class Node():

	def __init__(self, data):

		self.data = data
		self.next = None


class LinkedList():

	def __init__(self):

		
		self.head = None

	def remove_duplicates(self):

		ptr1 = None
		ptr2 = None
		dup = None
		ptr1 = self.head

		
		while (ptr1 != None and ptr1.next != None):

			ptr2 = ptr1

			
			
			while (ptr2.next != None):

				
				if (ptr1.data == ptr2.next.data):

					
					dup = ptr2.next
					ptr2.next = ptr2.next.next
				else:
					ptr2 = ptr2.next

			ptr1 = ptr1.next

	
		def printList(self):
		temp = self.head

		while(temp != None):
			print(temp.data, end=" ")
			temp = temp.next

		print()



list = LinkedList()
list.head = Node(10)
list.head.next = Node(12)
list.head.next.next = Node(11)
list.head.next.next.next = Node(11)
list.head.next.next.next.next = Node(12)
list.head.next.next.next.next.next = Node(11)
list.head.next.next.next.next.next.next = Node(10)

print("Linked List before removing duplicates :")
list.printList()
list.remove_duplicates()
print()
print("Linked List after removing duplicates :")
list.printList()
