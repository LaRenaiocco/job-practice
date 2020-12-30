# HACKERRANK 
# MERGE POINT OF TWO LINKED LISTS 

#Lines 5-39 included with hackerrank problem
import math
import os
import random
import re
import sys

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

# Complete the findMergeNode function below.
# Taking in 2 head nodes.  Return node value where 2 lists converge to 1
# pseudocode:
# traverse through one list and make list of nodes 
# traverse through second list and make list of nodes.
# loop through list one and list two
# if node == eachother, return value

def findMergeNode(head1, head2):
    list_1 = []
    list_2 = []
    current_1 = head1
    current_2 = head2
    while current_1:
        list_1.append(current_1)
        current_1 = current_1.next
    while current_2:
        list_2.append(current_2)
        current_2 = current_2.next
    print(list_1)
    print(list_2)
    for x in list_1:
        for y in list_2:
            if x == y:
                return x.data