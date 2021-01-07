#Hacker Rank
#Merge sort of two already sorted linked lists
#lines 4-32 are included in code stub on hacker rank
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

#
#while either head is not none:
#first check if current1 is none.
#   if yes, add current2
#   increase current2
#check same for cuurent2 is none?
#check if current 1 is less that current2
#   if yes, add current 1
#   increase current1
#check same for current2 is less than current1
#else we can assume 1 and 2 are equal
#   then we add both one and two 
#   and increase 1 and 2
def mergeLists(head1, head2):
    new_head = None
    new_current = None
    current1 = head1
    current2 = head2
    
    if current1.data == None:
        return current2
    elif current2.data == None:
        return current1
    elif current1.data < current2.data:
        new_current = current1
        new_head = new_current
        current1 = current1.next
    else:
        new_current = current2
        new_head = new_current
        current2 = current2.next
    
    while current1 != None or current2 != None:
        if current1 == None:
            new_current.next = current2
            new_current = new_current.next
            current2 = current2.next
        elif current2 == None:
            new_current.next = current1
            new_current = new_current.next
            current1 = current1.next
        elif current1.data <= current2.data:
            new_current.next = current1
            new_current = new_current.next
            current1 = current1.next
        else:
            new_current.next = current2
            new_current = new_current.next
            current2 = current2.next
        
    return new_head
            
            
    
    