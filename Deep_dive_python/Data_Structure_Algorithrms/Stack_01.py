class Stack(object):
    def __init__(self):
        self.stack = []
        self.num_items = 0
    
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.insert(self.num_items, data)
        self.num_items += 1
        return f"{data} pushed to stack {self.stack}"
    
    def pop_item(self):
        self.num_items -= 1
        data = self.stack.pop(self.num_items)
        return f"{data} pop from stack {self.stack}"
    

s = Stack()
print(s.push(2))
print(s.push(4))
print(s.push(6))
print(s.pop_item())