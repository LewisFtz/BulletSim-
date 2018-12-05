import matplotlib.pyplot as plt
import math
import stack_rev

def displacement_graph(self,initial_velocity,height):  #Horizontal displcament 
    #height = 1.5 # height     #1 Vertical
    displacement = 0       #2 Horizontal
    initial_velocity = self.initial_velocity
    height = self.height
    height = float(height)

    initial_velocity = float(initial_velocity)
    vert_velocity = 0          #V1
    horiz_velocity = 0          #V2
    vert_acceleration = 9.81    #A1
    horiz_acceleration = 0       #A2   
                       #T
    vert_initial_velocity = initial_velocity * math.sin(0.7853981634)  #U1
    horiz_initial_velocity = initial_velocity * math.cos(0.7853981634)  #U2
    #print (vert_initial_velocity)
    
    time = ((2*height)/(vert_acceleration))**0.5
    print (time)
    horiz_acceleration = (horiz_velocity - horiz_initial_velocity)/time
    #print(horiz_acceleration)

    displacement = time * horiz_initial_velocity
    #print (displacement)
       
    time = float(time)
    variable = ( (time) * (100) )
    variable = int(variable)
    stack =[]
    #print (variable)
    #print (time)
    displacement = int(displacement)
    X = time
    for i in range(variable):
        i = i /1000
        displacment = (i * horiz_initial_velocity)
        #print (i)
        displacment = ( (displacment) * (1000) )
        displacment = round(displacment, 0)
        displacment = str(displacment)
        
        stack.append(displacment)
    total_stack = stack.copy() #Uses stack to flip the values. 
    print (stack)
    reverse_stack=stack_rev.Stack.reverse(stack)
##
##    def isEmpty(stack):
##        if len(stack) == 0:
##            print ('size')
##            return true
##    
##    def pop(stack):
##        if isEmpty(stack): return
##        #print ('pop')
##        top_of_stack=stack.pop()
##
##        return top_of_stack
##        
##    def reverse(stack):
##        n = len(stack)
##        #print(n)
##        reverse_stack = []
##        for i in range(0,n):
##            reverse_stack.append(pop(stack))
##        #print (reverse_stack)
##        return reverse_stack
    
    

    total_stack.extend(reverse_stack)
    plt.plot(total_stack)
    plt.ylabel('Vert Displacement(m) ')
    plt.xlabel('Time(S)')
    plt.show() 
