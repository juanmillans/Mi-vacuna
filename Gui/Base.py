import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU
from Gui.Home import Home
from Gui.OP1 import OP1
from Gui.OP2 import OP2
from Gui.OP3 import OP3
from Gui.OP4 import OP4
from Gui.OP6 import OP6



class Base:
  def  __init__(self):
    self.name = "rrrra"
    self.id = "rra"
    self.procesor = CPU("personalData")



#---------------------MAIN WINDOW INIZIALIZATION-----------------    
    p_windw=tk.Tk()
    p_windw.title("  Nuestra vacuna ")
    
    self.Ojana=Home(p_windw)
    self.first = OP1(p_windw)
    self.second=OP2(p_windw)
    self.third=OP3(p_windw)
    self.fourth=OP4(p_windw)
    self.sixth=OP6(p_windw)
#---------------------Image inizialization -----------------
    Ph=PhotoImage(file = 'Gui/I.png') # ICONO DE MI VACUNA 
    icon=PhotoImage(file = 'Gui/V.png') # ICONO Grande 

 
    p_windw.iconphoto(False, Ph)
#---------------------MAIN WINDOW GRID CONFIGURATION-----------------       
    p_windw.columnconfigure(index=0,    
                           )

    p_windw.rowconfigure(index=0
                        )


    
    p_windw.rowconfigure(index=1,weight=1
                           )
    p_windw.columnconfigure(index=1,weight=1
                           )

                           
#---------------------FRAME INITIALIZATION-----------------
    iconframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5,width=20,height=20)
    
    self.descriptionframe=self.Ojana.descriptionframe
    self.methodsframe=self.Ojana.methodsframe
    buttonframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5,
                              bg="#ADD5FF")
#self.Ojana.methodsframe

#---------------------FRAME INITIALIZATION-----------------
    iconframe.config(width=2,height=2)
    iconframe.grid_propagate(0)

#--------------------- LABELS INITIALIZATION----------------- 
    imagelbl= tk.Label(master=iconframe,image=icon,
                     padx = 1, pady = 1) 
    labl0 = tk.Label(master=self.descriptionframe,
                     text = "Para mostrar la opcion deseada presione el numero que se encuentra\nal lado de la opcion deseada ",
                     padx = 1, pady = 1,justify="left")    


#---------------------FRAME POSITION-----------------
    iconframe.grid(row=0,column=0,sticky="NSEW")
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    buttonframe.grid(row=1,column=0,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")


#---------------------BUTTONS INITIALIZATION-----------------    
    button1 = tk.Button(master=buttonframe, text = "1", padx = 35, pady = 10
                        ,command=self.BTN1,bg="#2892B8")
    button2 = tk.Button(master=buttonframe, text = "2", padx = 35, pady = 10
                        ,command=self.BTN2,bg="#2892B8")
    button3 = tk.Button(master=buttonframe, text = "3", padx = 35, pady = 10
                        ,command=self.BTN3,bg="#2892B8")
    button4 = tk.Button(master=buttonframe, text = "4", padx = 35, pady = 10
                        ,command=self.BTN4,bg="#2892B8")
    button5 = tk.Button(master=buttonframe, text = "5", padx = 35, pady = 10,command=self.BTN5,bg="#2892B8")
    button6 = tk.Button(master=buttonframe, text = "6", padx = 35, pady = 10,command=self.BTN6,bg="#2892B8")
    DONE = tk.Button(master=buttonframe, text = "Home", padx = 20, pady = 10,command=self.BTNH)
    

#---------------------BUTTON POSITION-----------------    
    
    button1.pack(pady=1,padx=0)
    button2.pack(pady=1,padx=0)
    button3.pack(pady=1,padx=0)
    button4.pack(pady=1,padx=0)
    button5.pack(pady=1,padx=0)
    button6.pack(pady=1,padx=0)
    DONE.pack(pady=20,padx=0)


#---------------------LABELS POSITION----------------- 
    imagelbl.grid(row=1,column = 0,sticky ="NSWE", padx = 1, pady =1)

    #self.Ojana.show_all()
    self.Ojana.show_all()
    
    #button=Button(p_windw)
    
    p_windw.mainloop()


  def BTN1(self):
    self.hide_everything()
    self.descriptionframe=self.first.descriptionframe
    self.methodsframe=self.first.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.first.show_Op1()

  def BTN2(self):
    self.hide_everything()
    self.descriptionframe=self.second.descriptionframe
    self.methodsframe=self.second.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.second.show_all()
    
  def BTN3(self):
    self.hide_everything()
    self.descriptionframe=self.third.descriptionframe
    self.methodsframe=self.third.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.third.show_all()
  def BTN4(self):
    self.hide_everything()
    self.descriptionframe=self.fourth.descriptionframe
    self.methodsframe=self.fourth.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.fourth.show_all()
  def BTN5(self):
    self.hide_everything()
    self.procesor.Vperperson_pie()
    self.descriptionframe=self.Ojana.descriptionframe
    self.methodsframe=self.Ojana.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.Ojana.show_all()
    
  def BTN6(self):
    self.hide_everything()
    self.descriptionframe=self.sixth.descriptionframe
    self.methodsframe=self.sixth.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.sixth.show_Op6()
    
    
  def BTNH(self):
    self.hide_everything()
    self.descriptionframe=self.Ojana.descriptionframe
    self.methodsframe=self.Ojana.methodsframe
    self.descriptionframe.grid(row=0,column=1,sticky="NSEW")
    self.methodsframe.grid(row=1,column=1,sticky="NSEW")
    self.Ojana.show_all()

    
  def hide_everything(self):
    (self.methodsframe).grid_forget()
    (self.descriptionframe).grid_forget()
    