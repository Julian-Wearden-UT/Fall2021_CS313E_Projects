#  File: TestBinaryTree.py

#  Description: This assignment adds helper methods for the Tree class developed in class.

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 10/30/2021

#  Date Last Modified: 11/01/2021


import sys


class Node(object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    # inserts data into l/r based on comparison with parent node
    def insert(self, data):
        # insert based on BST from class
        new_node = Node(data)

        current = self.root
        if current is None:
            self.root = new_node
        else:
            parent = self.root
            while current is not None:
                parent = current
                if data >= current.data:
                    current = current.rChild
                else:
                    current = current.lChild

            if data >= parent.data:
                parent.rChild = new_node
            else:
                parent.lChild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        # If both empty trees
        if self.root is None and pNode.root is None:
            return True
        # If one not empty and other is
        elif self.root is not None and pNode.root is None:
            return False
        # If one empty and other not
        elif self.root is None and pNode.root is not None:
            return False
        else:
            return self.is_similar_rec(self.root, pNode.root)

    def is_similar_rec(self, qNode, pNode):
        # End of tree
        if qNode is None and pNode is None:
            return True
        # Current data and left path and right path all similar return true
        elif qNode.data == pNode.data and self.is_similar_rec(qNode.lChild, pNode.lChild) and self.is_similar_rec(
                qNode.rChild, pNode.rChild):
            return True
        else:
            return False

    # get_level not working properly but gradescope not providing test input so I have no clue what's going on
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        listLevels = []
        # Is empty tree
        if self.root is None:
            return []
        # Is tree with only root
        elif level == 1:
            listLevels.append(self.root)
            return listLevels
        # Is too large for tree
        elif self.get_height() > level:
            return []
        else:
            self.get_level_rec(self.root, level, listLevels, 1)
            return listLevels

    def get_level_rec(self, pNode, level, listLevels, current):
        # Reach end of tree
        if pNode is None:
            return []
        # Found level
        elif current == level:
            listLevels.append(pNode)
            return listLevels
        # Left and right paths
        self.get_level_rec(pNode.lChild, level, listLevels, current + 1)
        self.get_level_rec(pNode.rChild, level, listLevels, current + 1)
        return listLevels

    # Returns the height of the tree
    # should height include root? or root = 0, so height - 1?
    def get_height(self):
        # If tree is empty height = 0
        if self.root is None:
            return 0
        else:
            return self.get_height_rec(self.root)

    def get_height_rec(self, node):
        if node is None:
            return 0
        # Check both left and right paths of node
        leftPath = self.get_height_rec(node.lChild)
        rightPath = self.get_height_rec(node.rChild)
        # return highest value (+1 for root)
        return max(leftPath, rightPath) + 1

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        # 0 Nodes if tree is empty
        if self.root is None:
            return 0
        else:
            return self.num_nodes_rec(self.root)

    def num_nodes_rec(self, node):
        # Don't add 1 to counter
        if node is None:
            return 0
        # Add number in left subtree + number in right subtree + 1 for root
        else:
            return self.num_nodes_rec(node.lChild) + self.num_nodes_rec(node.rChild) + 1


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints


if __name__ == "__main__":
    main()

# python3 TestBinaryTree.py < bst.in
