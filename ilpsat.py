from pulp import *
from collections import defaultdict

class AND:
    def __init__(self, inputOne, inputTwo, output):
        self.inputOne = inputOne
        self.inputTwo = inputTwo

    def getOut(self):
        return self.inputOne and self.inputTwo

class OR:
    def __init__(self, inputOne, inputTwo, output):
        self.inputOne = inputOne
        self.inputTwo = inputTwo

    def getOut(self):
        return self.inputOne or self.inputTwo

class NOT:
    def __init__(self, inputOne):
        self.inputOne = inputOne

def main():
    test_binary_problem = LpProblem('ILPSAT', LpMaximize)

    for i in enumerate(graph):
        test_binary_variable = LpVariable('x{}'.format(i + 1), 0, 1, LpBinary)
