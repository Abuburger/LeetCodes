import operator #For Revese Polish Notation 
from collections import defaultdict

#Valid Parentheses
def isValid(s: str) -> bool:
    hashmap = {"[" : "]", "{" : "}", "(" : ")"}
    open  = set(["[", "{", "("])
    stack = []
    for i in range(len(s)):
        if s[i] in open:
            stack.append(s[i])
        elif len(stack) == 0:
            return False
        elif s[i] != hashmap[stack[len(stack) - 1]]:
            return False
        else:
            stack.pop() 
        print(stack)
    return len(stack) == 0 

#Min Stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            mini = min(val, self.minstack[-1])
            self.minstack.append(mini)
            

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



# Evaluate Reverse Polish Notation
def EvalRPN(tokens: list[str]) -> int:
    operators = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv
    }
    stack = []
    for i in range(len(tokens)):
        if tokens[i] not in operators:
            stack.append(tokens[i])
        else: 
            operand1 = int(stack.pop())
            operand2 = int(stack.pop())
            stack.append(operators[tokens[i]](operand2, operand1))
    return int(stack.pop())

#Daily Temperature
temps = [30,38,30,36,35,40,28]
def dailyTemperature(temperatures: list[int]) -> list[int]:
    res = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures) -1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if len(stack) == 0:
                stack.append(i)
        else:
            res[i] = stack[-1] - i
            stack.append(i)

    return res

lrec = [1,3,7]
#Largest Rectangle In Histogram
def largestRectangleArea(heights: list[int]) -> int: 
    maxhist = 0 
    stack = []
    for i, n in enumerate(heights):
        start = i 

        while stack and n < stack[-1][1]:
            index, height = stack.pop() 
            area = height * (i - index) 
            maxhist = max(maxhist, area)
            start = index
        stack.append((start, n))

    for index, height in stack: 
        farea = height * (len(heights) - index)
        maxhist = max(maxhist, farea) 
    return maxhist

print(largestRectangleArea(lrec))

