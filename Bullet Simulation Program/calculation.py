import math

def max_velocity(initial_velocity, height):
    
    #Find max vertical velocity then do cos(45) of it to get its true velocity
    vert_acceleration = -9.81  # F = M * A
    height = (float(height))    
    initial_velocity = float(initial_velocity)
    #print (initial_velocity)
    vert_initial_velocity = (initial_velocity * math.sin(0.7853981634)) #0.78 is the 45degres but in radians 
    horiz_initial_velocity = (initial_velocity * math.cos(0.7853981634))       
    time_p2 = (0 - (vert_initial_velocity / vert_acceleration))    
    vert_velocity = (-vert_acceleration * time_p2)
    time_p3 = ((2*height) / (vert_velocity))
    #Need 3rd part as that is just before it hits the ground. Vetical displacemnt is 0 once it is at same height it is fired from 
    time = (time_p2 + time_p3) #Only want time that it is falling
    vert_velocity = (0 +(vert_acceleration) * (time) )#V = U +AT
    vert_velocity = -vert_velocity
    vert_velocity = (round(vert_velocity, 2)) 
    return vert_velocity


def air_resistance(initial_velocity,mass_of_bullet,height):#Calculation of Air resistance
    vert_acceleration = -9.81  # F = M * A
    k = 0.00001 #k has to be as close to 0 as possible but it being 0 would create a mathmatical error
    e = 2.71828 #Mathmatical varibale 
    height = (float(height))
    mass_of_bullet = (float(mass_of_bullet))
    mass_of_bullet = mass_of_bullet / 1000 #Conversion to kg
    mass_of_bullet = mass_of_bullet *vert_acceleration
    initial_velocity = float(initial_velocity)
    #print (initial_velocity)
    vert_initial_velocity = (initial_velocity * math.sin(0.7853981634))
    horiz_initial_velocity = (initial_velocity * math.cos(0.7853981634))
    time_p1 = (0 - (vert_initial_velocity / vert_acceleration))     
    time_p2 = time_p1 
    vert_velocity = (-vert_acceleration * time_p2)
    time_p3 = ((2*height) / (vert_velocity))
    time = (time_p1 + time_p2 + time_p3)
     ###horiz_acceleration = (0 - (horiz_initial_velocity) / time)
     #print (horiz_acceleration)
    horiz_acceleration =(( -k/mass_of_bullet * horiz_initial_velocity) * (e **(-k/mass_of_bullet * time)))

    air_resistance = horiz_acceleration
    air_resistance = (round(air_resistance, 4))#4 DP as otherwise it is negligable 
    return air_resistance 

def horiz_displacement(initial_velocity,height): #CORRECT    

    vert_acceleration = -9.81
    initial_velocity = float(initial_velocity)
    height = (float(height))
    #print (height)
    
    vert_initial_velocity = (initial_velocity * math.sin(0.7853981634))#inital ADD TO ALL INITAIL THINGSS
    horiz_initial_velocity = (initial_velocity * math.cos(0.7853981634))

    time_p1 = (0 - (vert_initial_velocity / vert_acceleration))  # This is to max height 
    time_p2 = time_p1 # Calculate time to start point then distance to grounds
    vert_velocity = (-vert_acceleration * time_p2) #V = U + AT So V = 9.81 * time_p2 
    time_p3 = ((2*height) / (vert_velocity))#2S = (U+V) * T    S is height so 2S/U  U is V at timeP1+P2
    #print (time_p3)
    time = (time_p1 + time_p2 + time_p3)
    horiz_displacement = time * horiz_initial_velocity
    horiz_displacement = horiz_displacement / 1609 #Conversion to miles
    horiz_displacement = (round(horiz_displacement, 2))
    return horiz_displacement

