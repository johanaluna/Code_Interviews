class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        #initialize the list with an empty head
        self.head = None
    
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node
        else:
            new_node = Node(data)
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            new_node.prev = currentNode
            currentNode.next = new_node
            
    def remove(self, data):
        currentNode = self.head
        if currentNode.data == data:
            currentNode = currentNode.next
            self.head = currentNode
            currentNode.prev = None
        else:
            while currentNode.next:
                if currentNode.next.data == data:
                    pivot = currentNode.next
                    currentNode.next = pivot.next
                    currentNode.next.prev = currentNode
                    break
                else:
                    currentNode = currentNode.next

            if currentNode.next == None:
                print("Error: not in list")

    def printList(self):
        currentNode = self.head
        completeList = []
        while currentNode:
            completeList.append(currentNode.data)
            currentNode = currentNode.next
        return completeList

    def lenghtList(self):
        count = 0 
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count

dll = LinkedList()

dll.append(1)
dll.append(2)
dll.append(4)
dll.append(6)
dll.append(7)
dll.append(9)

print(dll.printList())
print(dll.lenghtList())

dll.remove(6)
print(dll.printList())
print(dll.lenghtList())

dll.remove(7)
print(dll.printList())
print(dll.lenghtList())

dll.remove(7)
print(dll.printList())
print(dll.lenghtList())

