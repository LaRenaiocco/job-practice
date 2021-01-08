# HACKERRANK Inset node into a doubly linked list.
# lines 3-34 provided by hackerrank
class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail =


    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



def sortedInsert(head, data):
    new_node = DoublyLinkedListNode(data)
    current = head
    
    if head == None:
        return new_node

    while current:
        print(current)
        if data < current.data:                         #insert at beginning of llist
            new_node.next = current
            current.prev = new_node
            return new_node
        elif current.next == None:                      #add node to end of llist
            current.next = new_node
            new_node.prev = current
            return head
        elif current.data <= data < current.next.data:   # insert in middle of llist
            current_next = current.next
            new_node = DoublyLinkedListNode(data)
            new_node.prev = current
            new_node.next = current.next
            current_next.prev = new_node
            current.next = new_node
            return head
        else:                                           # move to next node
            current = current.next

    #pseuodocode
    # create a variable to store current node assigned to head
    # traverse through linked list
    # check if insert node is > current and < current.next
    # if no:
    #     reassign current to current.next
    # if yes:
    #     create variable for next and assign to current.next
    #     reassign current.next to be input
    #     assign input.previous to be current
    #     assign input.next to be variable for current.next
    #     reassign variable for current.next's previous to be input
    