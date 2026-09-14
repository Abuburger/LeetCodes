#Valid Parentheses
s1 = "[]"
s2 = "([{}])"
s3 = "[(])"
s4 = "(){}}{"



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

print(isValid(s4))
