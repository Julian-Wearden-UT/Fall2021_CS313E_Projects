#  File: Josephus.py

# Description: This lab implements the Josephus problem using a circular linked list

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 10/16/2021

#  Date Last Modified: 10/17/2021

import sys


class Link(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None                       # head node

    # Insert an element (value) in the list
    def insert(self, data):
        newLink = Link(data)
        if self.first is None:                  # is first element
            self.first = newLink
            self.first.next = self.first
        else:                                   # is added element
            newLink.next = self.first.next
            self.first.next = newLink
            self.first = newLink

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        if current is None:                     # is empty
            return None
        elif current.data == data:              # is "first" element?
            return current
        else:                                   # else check the rest
            while current.next != self.first:
                if current.data == data:    # if found return
                    return current
                else:                       # else check next link
                    current = current.next

        return None

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        current = self.first

        if current is None:                                         # is empty
            return None
        elif current.next == self.first and current.data == data:   # single node
            self.first = None
            return current
        else:
            while current.next != self.first:                       # check all other nodes
                if current.next.data == data:
                    previous = current.next
                    current.next = current.next.next
                    return previous
                current = current.next

            if current.next.data == data:                           # check first node (since it was skipped earlier)
                previous = current.next
                current.next = current.next.next
                self.first = current
                return previous

        return None

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        if start.next == start:                     # single node
            self.first = None
            return start.data, None

        current = start
        for i in range(n - 1):                      # iterate to node to be removed
            current = current.next

        nextEl = current.next                       # save next link in nextEl
        removed = current.data                      # data removed from linked list
        self.delete(current.data)                   # actually remove node

        return removed, nextEl

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists (i.e [1, 2, ... , n])
    def __str__(self):
        if self.first is not None:                      # if link is not empty
            strng = "["
            current = self.first.next
            while current != self.first:                # iterate through link
                strng += str(current.data) + str(", ")  # add link data to string
                current = current.next
            strng += str(current.data) + "]"
            return strng
        else:                                           # empty link
            return "[]"


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    group = CircularList()                                      # create linked list
    for i in range(1, num_soldiers + 1):                        # insert soldiers as nodes in linked list
        group.insert(i)
    next = group.find(start_count)                              # next = current soldier
    if group.first is not None:                                 # if linked list not empty
        while group.first != group.first.next:                  # iterate through list
            removed, next = group.delete_after(next, elim_num)
            if removed is not None:
                print(removed)

        removed, next = group.delete_after(next, 1)             # print last remaining soldier number
        print(removed)


if __name__ == "__main__":
    main()
