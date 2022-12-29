import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU

from Data.Text_processor import people
# deathwing=Image.open('Deathwing.PNG')
# image2=deathwing.resize((100,50),Image.ANTIALIAS)
#Deathwing2=ImageTk.PhotoImage(image2)


class OP4:

  def __init__(self, p_windw):
    self.name = "rrrra"
    self.id = "rra"
    self.procesor = CPU("personalData")

    self.methodsframe = tk.LabelFrame(master=p_windw, padx=5, pady=5)
    self.descriptionframe = tk.LabelFrame(master=p_windw, padx=5, pady=5)

    self.labl0 = tk.Label(
      master=self.descriptionframe,
      text=
      "Esta funcion toma como entrada un numero de vacunas \ny entrega la cantidad de personas vacunadas con ese numero de vacunas",
      padx=1,
      pady=1,
      justify="left")
    #-------------------------LABELS INITIALIZATION---------------------------------------------
    self.labl1 = tk.Label(master=self.methodsframe,
                          text="Numero de Vacunas",
                          padx=1,
                          pady=1,
                          justify="left")
    self.labl2 = tk.Label(master=self.methodsframe,
                          text="",
                          padx=1,
                          pady=1,
                          justify="left")

    #---------------------------ENTRIES INIZIALIZATION----------------------------------
    self.Entry1 = tk.Entry(master=self.methodsframe,width=30)

    #---------------------------Buttons INIZIALIZATION----------------------------------
    self.submit = tk.Button(master=self.methodsframe,
                            text="Submit",
                            padx=20,
                            pady=10,
                            command=self.ShowDoses_Per_Person
                           )
  def ShowDoses_Per_Person(self):      
    F1=False
    try:
      D = int(self.Entry1.get() )
      d = int(D)
      if d >= 0 and d <= 7:
        F1=True
      else:
        self.Entry1.delete(0,'end')
        self.Entry1.insert(0," ingrese un valor entre 0 y 6 ")

    except ValueError:
      self.Entry1.delete(0,'end')
      self.Entry1.insert(0,"Ingrese un valor valido")


    if F1:
      message=f"{self.procesor.Vperperson(d)} "
      self.labl2.config(text=message)


  def show_all(self):

    self.labl0.grid(row=1, column=0, sticky="NSW", padx=5, pady=12)

    self.labl1.grid(row=0, column=0, sticky="NSW", padx=5, pady=5)
    self.labl2.grid(row=1, column=1, sticky="NSW", padx=5, pady=5)
    self.Entry1.grid(row=1, column=0, sticky="NSW", padx=5, pady=5)
    self.submit.grid(row=2, column=0, sticky="NSW", padx=5, pady=5)
