class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        
        if self.head == None:
            self.head = node
            self.tail = node
        else: 
            current = self.head
            node.next = current
            current.prev = node
            self.head = node
			
    def setTail(self, node):
        if self.tail == None:
            self.head = node
            self.tail = node
        else: 
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            self.tail = node

    def insertBefore(self, node, nodeToInsert):
        
        if self.head.value == node:
            self.setHead(nodeToInsert)
        else:
            current = self.head
            while current:
                if current.value == node:
                    current.prev.next = nodeToInsert
                    nodeToInsert.next = current
                    current.prev = nodeToInsert
                current = current.next

		

    def insertAfter(self, node, nodeToInsert):
        current = self.head
        while current.next:
            if current.value == node:
                nodeToInsert.prev = current 
                nodeToInsert.next = current.next
                current.next = nodeToInsert
            
            current = current.next
        self.setTail(nodeToInsert)

    def insertAtPosition(self, position, nodeToInsert):
        index = 0
        
        if self.head is None:
            self.setHead(nodeToInsert)
        else:
            current = self.head
            while current:
                if position == index :
                    self.insertBefore(current.value, nodeToInsert)
                index += 1
                current = current.next



    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass
    def printlist(self):
        currentNode = self.head
        completeList = []
        while currentNode:
            completeList.append(currentNode.value)
            currentNode = currentNode.next
        return completeList



dll = DoublyLinkedList()
a = Node(7)

dll.setHead(Node(7))
dll.setHead(Node(8))
print(dll.printlist())
dll.setTail(Node(9))
dll.setTail(Node(3))
print(dll.printlist())
dll.insertAfter(3, Node(4))
print(dll.printlist())
print("insert before")
dll.insertBefore(8, Node(2))
print(dll.printlist())
dll.insertBefore(4, Node(1))
print(dll.printlist())
print("At position ")
dll.insertAtPosition(6, Node(6))
print(dll.printlist())