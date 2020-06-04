# 1 --> 2 --> 3

 def __init__(self, x):
    self.val = x
    self.next = None 

def deleteNode(self,node):
    if self.val is None or self.next is None:
        return False
    
    if self.val is node:
        self.val = self.next.val
        self.next = self.next.next
        return True
    else: 
        self.next = self.next.next
    return False


