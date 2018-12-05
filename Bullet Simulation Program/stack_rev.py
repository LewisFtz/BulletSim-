###Stack class
class Stack():

    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self,stack):
        self.stack.append(stack)
        self.top += 1        

    def peek(self, stack):
       self.stack[self.top]
    
    def isEmpty(self, stack):
        if len(stack) == 0:
            print ('size')
            return true
     
    def pop(self, stack):
        if self.isEmpty(stack): return
        #print ('pop')
        top_of_stack=stack.pop()

        return top_of_stack
        
    def reverse(stack):
        #stack = self.stack
        n = len(stack)
        #print(n)
        print (stack)
        reverse_stack = []
        for i in range(0,n):
            reverse_stack.append(stack.pop())
        print (reverse_stack)
        return reverse_stack

    
