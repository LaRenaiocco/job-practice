# Delete duplicate value from linked list - HackerRank

# lines 4-32 provided by hackerrank
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


def removeDuplicates(head):
    previous = head
    current = head.next
    
    while current:
        if previous.data == current.data:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next
    return head