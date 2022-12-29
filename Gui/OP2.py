import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU

from Data.Text_processor import people
# deathwing=Image.open('Deathwing.PNG')
# image2=deathwing.resize((100,50),Image.ANTIALIAS)
#Deathwing2=ImageTk.PhotoImage(image2)


class OP2:

  def __init__(self, p_windw):
    self.name = "rrrra"
    self.id = "rra"
    self.procesor = CPU("personalData")

    self.methodsframe = tk.LabelFrame(master=p_windw, padx=5, pady=5)
    self.descriptionframe = tk.LabelFrame(master=p_windw, padx=5, pady=5)

    self.labl0 = tk.Label(
      master=self.descriptionframe,
      text=
      "Esta funcion toma como entrada un rango de tiempo comprendido entre\nel año inicial, mes inicial y año final y mes final ",
      padx=1,
      pady=1,
      justify="left")

    #-------------------------LABELS INITIALIZATION---------------------------------------------
    self.labl1 = tk.Label(master=self.methodsframe,
                          text="año 1",
                          padx=1,
                          pady=1,
                          justify="left")
    self.labl2 = tk.Label(master=self.methodsframe,
                          text="Mes 1 ",
                          padx=1,
                          pady=1,
                          justify="left")
    self.labl3 = tk.Label(master=self.methodsframe,
                          text="año 2",
                          padx=1,
                          pady=1,
                          justify="left")
    self.labl4 = tk.Label(master=self.methodsframe,
                          text="Mes 2 ",
                          padx=1,
                          pady=1,
                          justify="left")
    self.labl5 = tk.Label(master=self.methodsframe,
                          text="",
                          padx=1,
                          pady=1,
                          justify="left")

    #---------------------------ENTRIES INIZIALIZATION----------------------------------
    self.Entry1 = tk.Entry(master=self.methodsframe, width=30)
    self.Entry2 = tk.Entry(master=self.methodsframe, width=30)
    self.Entry3 = tk.Entry(master=self.methodsframe, width=30)
    self.Entry4 = tk.Entry(master=self.methodsframe, width=30)
    #---------------------------Buttons INIZIALIZATION----------------------------------
    self.submit = tk.Button(master=self.methodsframe,
                            text="Submit",
                            padx=20,
                            pady=10,
                            command=self.ShowAppliedDoses)

  def show_all(self):
    self.labl0.grid(row=1, column=0, sticky="NSW", padx=5, pady=12)

    self.labl1.grid(row=0, column=0, sticky="NSW", padx=5, pady=5)
    self.Entry1.grid(row=1, column=0, sticky="NSW", padx=5, pady=5)

    self.labl2.grid(row=2, column=0, sticky="NSW", padx=5, pady=5)
    self.Entry2.grid(row=3, column=0, sticky="NSW", padx=5, pady=5)

    self.labl3.grid(row=4, column=0, sticky="NSW", padx=5, pady=5)
    self.Entry3.grid(row=5, column=0, sticky="NSW", padx=5, pady=5)

    self.labl4.grid(row=6, column=0, sticky="NSW", padx=5, pady=5)
    self.Entry4.grid(row=7, column=0, sticky="NSW", padx=5, pady=5)
    self.submit.grid(row=8, column=0, sticky="NSWE", padx=5, pady=5)
    self.labl5.grid(row=5, column=1, sticky="NSWE", padx=5, pady=5)

  def ShowAppliedDoses(self):
    F1 = False
    F2 = False
    F3 = False
    F4 = False
    try:
      Y1 = int(self.Entry1.get())
      y1 = int(Y1)
      if y1 >= 2019 and y1 <= 2040:
        F1 = True
        #self.Entry1.insert(0,"True")

      else:
        self.Entry1.delete(0,'end')
        self.Entry1.insert(0, " ingrese un valor entre 2019 y 2040")

    except ValueError:
      self.Entry1.delete(0,'end')
      self.Entry1.insert(0, "Ingrese un año valido")

    try:
      M1 = int(self.Entry2.get())
      m1 = int(M1)
      if m1 >= 1 and m1 <= 12:
        F2 = True
      # self.Entry2.insert(0,"True")
      else:
        self.Entry2.delete(0,'end')
        self.Entry2.insert(0, " ingrese un numero entre 0 y 12")

    except ValueError:
      self.Entry2.delete(0,'end')
      self.Entry2.insert(0, "Ingrese un mes valido")

    try:
      Y2 = int(self.Entry3.get())
      y2 = int(Y2)
      if (y2 >= 2019 and y2 <= 2040) and (y2 >= y1):
        F3 = True
        #self.Entry3.insert(0,"True")
      else:
        if y1<2040:
          self.Entry3.delete(0,'end')
          self.Entry3.insert(0, f" ingrese un valor entre {Y1} y 2040")
        else:
          self.Entry3.delete(0,'end')
          self.Entry3.insert(0, f" ingrese un valor menor que  2040")

    except ValueError:
      self.Entry3.delete(0,'end')
      self.Entry3.insert(0, "Ingrese un año valido")

    try:
      M2 = int(self.Entry4.get())
      m2 = int(M2)
      if (m2 >= 1 and m2 <= 12):
        if int(Y2) == int(Y1):
          if (m2 > m1):
            F4 = True
            #self.Entry4.insert(0,"True")
          else:
            self.Entry4.delete(0,'end')
            self.Entry4.insert(0,
                               "el segundo mes debe ser mayor que el primero")
        else:
          F4 = True
          #elf.Entry4.insert(0,"True")

      else:
        self.Entry4.delete(0,'end')
        self.Entry4.insert(0, " ingrese un numero entre 0 y 12")

    except ValueError:
      self.Entry4.delete(0,'end')
      self.Entry4.insert(0, "Ingrese un mes valido")

    if (F1 and F2 and F3 and F4) == True:
      result = (self.procesor.Ammount_of_vaccines(Y1, M1, Y2, M2))
      mensaje = f"Se vacunaron {result} personas entre las fechas \n{M1}/{Y1} Y {M2}/{Y2} "
      self.labl5.config(text=mensaje)
