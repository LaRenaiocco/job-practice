#Delete a node from a linked list (HackerRank)
def deleteNode(head, position):
    # handles head being deleted
    if position == 0:
        if head.next == None:
            return None
        else:
            new_head = head.next
            return new_head
    #handles all other positions in linked list
    index = 0
    previous = None
    current = head
    while index < position:
        index += 1
        previous = current
        current = current.next
    if current.next:
        previous.next = current.next
    else:
        previous.next = None
    return head
