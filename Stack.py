import operator #For Revese Polish Notation 

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


t1 = ["2","1","+","3","*"]
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
EvalRPN(t1)     
