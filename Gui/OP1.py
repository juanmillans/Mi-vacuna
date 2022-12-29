import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU
from Data.Text_processor import people
class OP1:
  def  __init__(self, p_windw):
    self.name = "rrra"
    self.id = "rra"
    self.procesor = CPU("personalData")

    self.methodsframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5)
    self.descriptionframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5)

    self.labl0 = tk.Label(master=self.descriptionframe,
                     text = "Esta función toma como entrada un rango de edad, para mostrar la cantidad de personas vacunadas",
                     padx = 1, pady = 1,justify="left")   



    
#-------------------------LABELS INITIALIZATION---------------------------------------------
    self.labl1 = tk.Label(master=self.methodsframe,
                     text = "Edad 1",
                     padx = 1, pady = 1,justify="left")
    self.labl2 = tk.Label(master=self.methodsframe,
                     text = "Edad 2 ",
                     padx = 1, pady = 1,justify="left")
    self.labl3 = tk.Label(master=self.methodsframe,
                     text = "",
                     padx = 1, pady = 1,justify="left")
#---------------------------ENTRIES INIZIALIZATION----------------------------------
    self.Entry1 = tk.Entry(master=self.methodsframe,width=30)
    self.Entry2= tk.Entry(master=self.methodsframe,width=30)
    self.submit = tk.Button(master=self.methodsframe, text = "Submit", padx = 20, pady = 10, command=self.readEntry_Op1)


  def  show_Op1(self):
    self.labl0.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 12)
  
    self.labl1.grid(row=0,column = 0, sticky ="NSW", padx = 5, pady = 5)    
    self.Entry1.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 5)
  
      
    self.labl2.grid(row=2,column = 0, sticky ="NSW", padx = 5, pady = 5)
    self.Entry2.grid(row=3,column = 0, sticky ="NSW", padx = 5, pady = 5)

    self.labl3.grid(row=5,column = 1, sticky ="NSWE", padx = 5, pady = 5)

    self.submit.grid(row=8,column = 0, sticky ="NSWE", padx = 5, pady = 5)
    
  def readEntry_Op1(self):
    F1=False
    F2=False

    try:
      Y1 = self.Entry1.get().strip()
      y1 = int(Y1)
      if y1 >= 0 and y1 <= 200:
        F1=True
      else:
        self.Entry1.delete(0,'end')
        self.Entry1.insert(0," ingrese un valor entre 0 y 200")

      

    except ValueError:
      self.Entry1.delete(0,'end')
      self.Entry1.insert(0,"Ingrese un año valido")



    try:
      Y2 = self.Entry2.get().strip()
      y2 = int(Y2)
      if y2 >= y1 and y2 <= 200:
        F2=True
      else:
        if y1>200:
          self.Entry2.delete(0,'end')
          self.Entry2.insert(0,f" ingrese un valor menor o igual a 200")
        else:  
          self.Entry2.delete(0,'end')
          self.Entry2.insert(0,f" ingrese un valor entre {y1} y 200")

    except ValueError:
      self.Entry2.delete(0,'end')
      self.Entry2.insert(0,"Ingrese un año valido")
    if (F1 and F2)==True:
      result=(self.procesor.V_AgeRange(y1, y2))
      mensaje=f"Se vacunaron {result} personas entre las edades \n{y1} y {y2} "
      self.labl3.config(text=mensaje)