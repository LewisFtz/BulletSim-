import matplotlib.pyplot as plt
import math

def velocity_graph(self,initial_velocity):
    
        initial_velocity = self.initial_velocity
        print (initial_velocity)
        initial_velocity = float(initial_velocity)
        vert_velocity = 0
        horiz_velocity = 0
        vert_acceleration = -9.81
        horiz_acceleration = 0
        time = 0
        vert_initial_velocity = initial_velocity * math.sin(0.7853981634)
        horiz_initial_velocity = initial_velocity * math.cos(0.7853981634)



        #print (U2)
        time = ( (vert_velocity - vert_initial_velocity) / vert_acceleration)
        horiz_acceleration = ( (horiz_velocity - horiz_initial_velocity) / time)
                
        List =[]
        time = int(time)
        #X = time
        horiz_initial_velocity = int(horiz_initial_velocity)
        for i in range(1):
            horiz_initial_velocity = horiz_initial_velocity - 1 
            for i in range(time):
                horiz_velocity = horiz_initial_velocity + (horiz_acceleration * i)
                #print (i,V2)
                List.append(horiz_velocity)
            
            for i in range(time):
                horiz_velocity = 0 + (horiz_acceleration * i)
                #print (i,V2)
                List.append(horiz_velocity)
        
            plt.plot(List)
            plt.ylabel('Velocity ')
            plt.xlabel('Time')
            plt.show()  
