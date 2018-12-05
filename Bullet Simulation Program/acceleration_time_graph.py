import matplotlib.pyplot as plt
import math

def acceleration_graph(self,initial_velocity,mass_of_bullet):
    
        initial_velocity = self.initial_velocity
        mass_of_bullet = self.mass_of_bullet
        mass_of_bullet = float(mass_of_bullet)
        print (initial_velocity)
        initial_velocity = float(initial_velocity)
        vert_velocity = 0
        horiz_velocity = 0
        vert_acceleration = -9.81
        horiz_acceleration = 0
        time = 0
        e = 2.71828
        k = 0.0001
        vert_initial_velocity = initial_velocity * math.sin(0.7853981634)
        horiz_initial_velocity = initial_velocity * math.cos(0.7853981634)


        time = ( (vert_velocity - vert_initial_velocity) / vert_acceleration)
        
        horiz_acceleration =(( -k/mass_of_bullet * horiz_initial_velocity) * (e **(-k/mass_of_bullet * time)))
        # ^ The drag equation 
        print (horiz_acceleration)        
        List =[]
        time = int(time)
        print (time)

        horiz_acceleration = (-horiz_acceleration)
        for i in range(1):
            
            for i in range(time):
                vert_acceleration = vert_acceleration                
                List.append(vert_acceleration)
            
            for i in range(time):
                horiz_acceleration = (horiz_acceleration)
                List.append(horiz_acceleration)

        plt.plot(List)
        plt.ylabel('Acceleration ')
        plt.xlabel('Time')
        plt.show()  
