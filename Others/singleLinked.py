class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

# single linked List 
class SLL:
    def __init__(self):
        self.root = Node()
    
    def addEnd(self, value):
        # create a node and passing the value
        new_node = Node(value)
        currentNode = self.root
        # go through the list and find the last node
        while currentNode.next!=None:
            currentNode = currentNode.next
        # set the next to the last node
        currentNode.next = new_node
    
    def length(self):
        size = 0
        currentNode = self.root
        while currentNode.next!=None:
            currentNode = currentNode.next
            size += 1
        return size
    
    def printList(self):
        currentNode = self.root
        nodes = []
        while currentNode.next!=None:
            currentNode = currentNode.next
            nodes.append(currentNode.value)
        print(nodes)
    
    def addAfter():
        pass

    def addBefore():
        pass

    def deleteNode():
        pass

single_linked = SLL()
single_linked.printList()

single_linked.addEnd(1)
single_linked.addEnd(8)
single_linked.addEnd(4)

single_linked.length()
single_linked.printList()