class Stack:

    def __init__(self, array = None):
        '''Constructor of class stack'''

        self.array = [] if array is None else array
    
    def __str__(self):
        '''Returns the stack description'''
        return f"The array has {self.size()} elements, the last element is {self.peek()}, and all the elements look like {self.array} "

    def push(self, value):
        '''push value to the top of the array'''
        self.array.append(value)

    def pop(self):
        '''returns value from the top of the stack and removes it'''
        if self.is_empty(): return -1 #handles case where there is nothing in the array
        return self.array.pop()
    
    def peek(self):
        '''Returns value from the top of the stack'''
        if self.is_empty(): return -1 #handles case where there is nothing in the array
        return self.array[-1]
    
    def is_empty(self):
        '''Returns true if stack is empty'''
        return len(self.array) == 0
    
    def size(self):
        '''Returns the size of the stack'''
        return len(self.array)
    
    