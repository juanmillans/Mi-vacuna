import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU

from Data.Text_processor import people
# deathwing=Image.open('Deathwing.PNG')
# image2=deathwing.resize((100,50),Image.ANTIALIAS)
#Deathwing2=ImageTk.PhotoImage(image2)

class OP3:
  def  __init__(self,p_windw):
    self.name = "rrrra"
    self.id = "rra"
    self.procesor = CPU("personalData")

    self.methodsframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5)
    self.descriptionframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5,bg="#70CBFF")

    self.labl0 = tk.Label(master=self.descriptionframe,
                     text = "Esta funcion toma como entrada un año\ny entrega una grafica de la apliicacion de vacunas en ese año ",
                     padx = 1, pady = 1,justify="left",bg="#70CBFF")   



    
#-------------------------LABELS INITIALIZATION---------------------------------------------
    self.labl1 = tk.Label(master=self.methodsframe,
                     text = "año",
                     padx = 1, pady = 1,justify="left")


#---------------------------ENTRIES INIZIALIZATION----------------------------------
    self.Entry1 = tk.Entry(master=self.methodsframe,width=30)

#---------------------------Buttons INIZIALIZATION----------------------------------
    self.submit = tk.Button(master=self.methodsframe, text = "Submit", padx = 20, pady = 10,command=self.ShowDosesPerMonth)
  def  show_all(self):
    
    self.labl0.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 12)

    self.labl1.grid(row=0,column = 0, sticky ="NSW", padx = 5, pady = 5)    
    self.Entry1.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 5)
    self.submit.grid(row=2,column = 0, sticky ="NSW", padx = 5, pady = 5)

  def ShowDosesPerMonth(self):
    F1=False
    
    try:
      Y = int( self.Entry1.get())
      y = int(Y)
      if y >= 2019 and y <= 2040:
        F1=True
        #self.Entry1.insert(0,"True")
      else:
        self.Entry1.delete(0,'end')
        self.Entry1.insert(0," ingrese un valor entre 2019 y 2040")

    except ValueError:
      self.Entry1.delete(0,'end')
      self.Entry1.insert(0,"Ingrese un año valido")

    if F1==True:
      self.procesor.Vaccines_per_month(Y)
