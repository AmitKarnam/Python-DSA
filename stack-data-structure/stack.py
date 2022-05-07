""" Stack Data Structure """

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()
        
    def topOfStack(self):
        return self.stack[-1]
    
    def isEmpty(self):
        return self.stack == []