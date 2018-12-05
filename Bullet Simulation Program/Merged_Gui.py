from tkinter import *   

import calculation
import matplotlib.pyplot as plt
import math
import velocity_time_graph
import displacement_time_graph
import acceleration_time_graph
import validation

class BulletGui():

    def __init__(self,master):
        self.master = master
        self.master.configure(background='azure3')
        self.master.title("Bullet Simulation")
        self.master.option_add('*Font', 'Georgia 12')
        self.master.option_add('Label.Font', 'Georgia 14 bold')
        self.master.option_add('*Background', 'azure3')
        self.master.option_add('*Entry.Background', 'azure2')
        self.master.geometry('900x360+150+100') #w,h,x,y
        self.top()
        self.middle()
        self.bottom()
        
    def top(self):        
        top_frame=Frame(self.master)        
        lbl_header=Label(top_frame)
        lbl_header.config(text="Bullet Simulation", font='Georgia 32 bold')
 
        top_frame.grid_rowconfigure(0,minsize=150)
        top_frame.grid(row=0)

        lbl_header.grid(row=0, column=1, padx=20)



    def middle(self):
        mid_frame=Frame(self.master)

        #Label for initial velocity
        lbl_initial_velocity = Label(mid_frame)
        lbl_initial_velocity.config(text='Enter initial velocity (m/s): ')

        #Label for mass of bullet
        lbl_mass_of_bullet = Label(mid_frame)
        lbl_mass_of_bullet.config(text='Enter mass of bullet (g): ')

        #Label height of user
        lbl_height = Label(mid_frame)
        lbl_height.config(text='Enter your height (m): ')

        #Label for max velocity - output
        lbl_max_velocity = Label(mid_frame)
        lbl_max_velocity.config(text='Max velocity of bullet (m/s): ')

        #Label for Air Resistance - output
        lbl_air_resistance  = Label(mid_frame)
        lbl_air_resistance .config(text='Air Resistance of bullet (N): ')
        
        #Label for displacemnt - output
        lbl_horiz_displacement = Label(mid_frame)
        lbl_horiz_displacement.config(text='Displacment of bullet (M): ') 


        
        #Text Entry - initial velocity 
        self.initial_velocity=StringVar(mid_frame)
        txt_initial_velocity = Entry(mid_frame)
        txt_initial_velocity.config(textvariable=self.initial_velocity,  width=20)

        #Text Entry - mass of bullet 
        self.mass_of_bullet=StringVar(mid_frame)
        txt_mass_of_bullet = Entry(mid_frame)
        txt_mass_of_bullet.config(textvariable=self.mass_of_bullet,  width=20)

        #Text Entry - height
        self.height=StringVar(mid_frame)
        txt_height = Entry(mid_frame)
        txt_height.config(textvariable=self.height,  width=20)
        
        #Text Entry - max velocity - output
        self.max_velocity=StringVar(mid_frame)
        txt_max_velocity = Entry(mid_frame)
        txt_max_velocity.config(textvariable=self.max_velocity,  width=20)
        
        #Text Entry - Air Resistance - output
        self.air_resistance = StringVar(mid_frame)
        txt_air_resistance  = Entry(mid_frame)
        txt_air_resistance.config(textvariable=self.air_resistance, width=20)

        #Text Entry -  displacemnt - output
        self.horiz_displacement=StringVar(mid_frame)
        txt_horiz_displacement = Entry(mid_frame)
        txt_horiz_displacement.config(textvariable=self.horiz_displacement,  width=20)


        mid_frame.grid_columnconfigure(0,minsize=100)
        mid_frame.grid(row=1, sticky='w')

                
        #row 0 of middle section
        lbl_initial_velocity.grid(row=0, column=0, sticky='e', padx=10)
        txt_initial_velocity.grid(row=0, column=1, padx=10)
        
        lbl_max_velocity.grid(row=0, column=2, sticky='e', padx=10)
        txt_max_velocity.grid(row=0, column=3, padx=10)
        
        
        #row 1
        lbl_mass_of_bullet.grid(row=1, column=0, sticky='e', padx=10)
        txt_mass_of_bullet.grid(row=1, column=1, padx=10)
        
        lbl_air_resistance.grid(row=1, column=2, sticky='e', padx=10)
        txt_air_resistance.grid(row=1, column=3, padx=10)

        #row 2
        lbl_height.grid(row=2, column=0, sticky='e', padx=10)
        txt_height.grid(row=2, column=1, padx=10)
        
        lbl_horiz_displacement.grid(row=2, column=2, sticky='e', padx=10)
        txt_horiz_displacement.grid(row=2, column=3, padx=10)


    def bottom(self):
        bottom_frame=Frame(self.master)
        
        #Telling which boxes they need to fill in 
        self.useful_msg=StringVar(bottom_frame)
        self.useful_msg.set("Fill in all text boxes on the left.")
        self.lbl_msg = Label(bottom_frame) 
        self.lbl_msg.config(textvariable=self.useful_msg, fg='grey4', width=50)
        
        #Calculation button to give outputs 
        btn_calculate=Button(bottom_frame)
        btn_calculate.config(text='Calculate', borderwidth=2, padx=0)
        btn_calculate.bind('<Button-1>',self.suvat)#####Runs def suvat

        #show graphs - new window(graph gui)
        btn_graphs=Button(bottom_frame)
        btn_graphs.config(text='View Graphs', borderwidth=2, padx=0)
        btn_graphs.bind('<Button-1>',self.graphs)

        bottom_frame.grid_rowconfigure(0,minsize=100)
        bottom_frame.grid(row=2)
        
        #row 0
        self.lbl_msg.grid(row=0, column=0)
        
        
        #row 1
        btn_calculate.grid(row=1, column=0, sticky='w', padx=50)
        btn_graphs.grid(row=1, column=3, sticky='e', padx=10)

    def suvat(self,event):
        self.max_velocity.set(0)##Resets the current values so new ones can be calculated
        self.horiz_displacement.set(0)
        self.air_resistance.set(0)
        
        height = self.height.get()
        initial_velocity = self.initial_velocity.get()
        mass_of_bullet = self.mass_of_bullet.get()
        validate = validation.validate(initial_velocity, height, mass_of_bullet)
        if validate == False:
            max_velocity = calculation.max_velocity(initial_velocity, height)
            horiz_displacement = calculation.horiz_displacement(initial_velocity, height)
            air_resistance = calculation.air_resistance(initial_velocity, mass_of_bullet,height)
            self.max_velocity.set(max_velocity)
            self.horiz_displacement.set(horiz_displacement)
            self.air_resistance.set(air_resistance)
        else:
            self.useful_msg.set("Invalid inputs, make sure they are all numbers")
    

        
    def graphs(self,event):
        #import graphs_gui
        initial_velocity = self.initial_velocity.get()
        height = self.height.get()
        mass_of_bullet = self.mass_of_bullet.get()
        self.newWindow = Toplevel(self.master)
        self.app=GraphsGui(self.newWindow,initial_velocity,height,mass_of_bullet)
        


class GraphsGui():

    def __init__(self,master,initial_velocity, height, mass_of_bullet):
        self.initial_velocity = initial_velocity
        self.height = height
        self.mass_of_bullet = mass_of_bullet
        self.master = master
        self.master.configure(background='azure3')
        self.master.title("Bullet Simulation")
        self.master.option_add('*Font', 'Georgia 12')
        self.master.option_add('Label.Font', 'Georgia 14 bold')
        self.master.option_add('*Background', 'azure3')
        self.master.option_add('*Entry.Background', 'azure2')
        self.master.geometry('400x200+400+490') #w,h,x,y
        self.top()
        self.middle()
        self.bottom()
        
    def top(self):        
        top_frame=Frame(self.master)        
        lbl_header=Label(top_frame)
        lbl_header.config(text="Bullet Simulation - Graphs ", font='Georgia 18 bold')

        top_frame.grid_rowconfigure(0,minsize=150)
        top_frame.grid(row=0)

        lbl_header.grid(row=0, column=1, padx=20)



    def middle(self):   #GRAPHS
        mid_frame=Frame(self.master)
        self.useful_message=StringVar(mid_frame)
        self.useful_message.set("Velocity against Time graph")
        self.lbl_message = Label(mid_frame)
        self.lbl_message.config(textvariable=self.useful_message, fg='black', width = 20) 

        #Label for graph
        lbl_initial_velocity = Label(mid_frame)
        lbl_initial_velocity.config(text='Enter initial velocity: ')

        #row 0
        self.lbl_message.grid(row = 0, column = 0)


    def bottom(self):
        bottom_frame=Frame(self.master)


        #s/t button
        btn_displacement_time=Button(bottom_frame)
        btn_displacement_time.config(text='S/T', borderwidth=2, padx=0)
        btn_displacement_time.bind('<Button-1>',self.displacement_time)

        #v/t button
        btn_velocity_time=Button(bottom_frame)
        btn_velocity_time.config(text='V/T', borderwidth=2, padx=0)
        btn_velocity_time.bind('<Button-1>',self.velocity_time)
        
        #a/t button
        btn_acceleration_time=Button(bottom_frame)
        btn_acceleration_time.config(text='A/T', borderwidth=2, padx=0)
        btn_acceleration_time.bind('<Button-1>',self.acceleration_time)

        bottom_frame.grid_rowconfigure(0,minsize=50)
        bottom_frame.grid(row=2)
        
        #row 0
        btn_displacement_time.grid(row=0, column=1, sticky='w')
        btn_velocity_time.grid(row=0, column=2, sticky='w')
        btn_acceleration_time.grid(row=0, column=3, sticky='w')

    def velocity_time(self,event): #Opens #V/T graph
        initial_velocity = self.initial_velocity
        
        self.app=velocity_time_graph.velocity_graph(self,initial_velocity)


    def displacement_time(self,event): #Opens S/T graph
        initial_velocity = self.initial_velocity
        height = self.height
        
        self.app=displacement_time_graph.displacement_graph(self,initial_velocity,height)

    def acceleration_time(self,event): #Opens A/T graph
        initial_velocity = self.initial_velocity
        mass_of_bullet = self.mass_of_bullet
        print (initial_velocity)
        self.app=acceleration_time_graph.acceleration_graph(self,initial_velocity,mass_of_bullet)
##
##
def main():
    root = Tk()

    Gui = BulletGui(root)  
    root.mainloop() 
        
        
main()
