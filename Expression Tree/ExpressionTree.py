#  File: ExpressionTree.py

#  Description: This program reads expression.in from stdin and creates an expression tree

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 10/22/2021

#  Date Last Modified: 10/22/2021

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']


class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = Node()

        # Strings for post and pre-order process
        self.preStrng = ""
        self.postStrng = ""

    def store_expression(self, expr):
        listExpr = []

        # Convert multi char operators to single char to make binary tree easier
        expr = expr.replace('**', '^')
        expr = expr.replace('//', '@')
        for item in expr:
            listExpr.append(item)
        for i in range(len(listExpr)):
            if i >= len(listExpr):
                break
            if listExpr[i] == '.':
                floatNum = ""
                floatNum += listExpr.pop(i - 1)
                floatNum += listExpr.pop(i - 1)
                floatNum += listExpr.pop(i - 1)
                listExpr.insert(i - 1, floatNum)
        return listExpr

    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree(self, expr):
        stack = Stack()
        current = self.root

        expr = self.store_expression(expr)

        for item in expr:
            # Ignore spaces
            if item == ' ':
                pass

            # Current token is left parenthesis
            elif item == "(":
                current.lChild = Node()
                stack.push(current)
                current = current.lChild

            # Current token is right parenthesis
            elif item == ")":
                if not stack.is_empty():
                    current = stack.pop()

            # Current token is operator
            elif item in operators or item == '^' or item == '@':
                current.data = item
                stack.push(current)
                current.rChild = Node()
                current = current.rChild

            # Current token is operand
            else:
                current.data = item
                current = stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
        # End of tree section
        if aNode is None:
            return 0

        # Return value
        if aNode.lChild is None and aNode.rChild is None:
            return float(aNode.data)

        left = self.evaluate(aNode.lChild)  # Pursue left path
        right = self.evaluate(aNode.rChild)  # Pursue right path

        # Map operator to python expression
        if aNode.data == '+':
            return left + right
        elif aNode.data == '-':
            return left - right
        elif aNode.data == '*':
            return left * right
        elif aNode.data == '/':
            return left / right
        elif aNode.data == '@':
            return left // right
        elif aNode.data == '%':
            return left % right
        elif aNode.data == '^':
            return left ** right
        else:
            return 0

    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        if aNode is not None:
            self.preStrng += str(aNode.data) + " "
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)
        self.preStrng = self.preStrng.replace('^', '**')
        self.preStrng = self.preStrng.replace('@', '//')
        return self.preStrng

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        if aNode is not None:
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            self.postStrng += str(aNode.data) + " "
        self.postStrng = self.postStrng.replace('^', '**')
        self.postStrng = self.postStrng.replace('@', '//')
        return self.postStrng


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
