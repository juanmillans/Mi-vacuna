import tkinter as tk
from tkinter import *
from Business_logic.CPU import CPU
from Data.Text_processor import people
#registeredppl
class OP6:
  def  __init__(self, p_windw):
    self.name = "rrrra"
    self.id = "rra"
    self.procesor = people("personalData")
    self.diccionario=self.procesor.RegisteredId()


    self.methodsframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5)
    self.descriptionframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5,bg="#70CBFF")

    self.labl0 = tk.Label(master=self.descriptionframe,
                     text = "Esta función toma como entrada su nimero de identidad con el cual consigue su certificado \nsiempre y cuando se encuentre registrado en la base de datos",
                     padx = 1, pady = 1,justify="left",bg="#70CBFF")
    self.labl1 = tk.Label(master=self.methodsframe,
                     text = "Introduzca su numero de identidad",
                     padx = 1, pady = 1,justify="left")

    self.labl2 = tk.Label(master=self.methodsframe,
                     text = "Dirijase a los archivos y busque un archivo llamado 'certificate.txt'",
                     padx = 1, pady = 1,justify="left")

    self.labl3 = tk.Label(master=self.methodsframe,
                     text = "Ese documento no se encuentra registrado",
                     padx = 1, pady = 1,justify="left")

      
    self.Entry1 = tk.Entry(master=self.methodsframe)
    self.submit = tk.Button(master=self.methodsframe, text = "Submit", padx = 20, pady = 10,
                            command=self.DoCert)


    

  def  show_Op6(self):
    self.labl0.grid(row=1, column=0, sticky="NSW", padx=5, pady=12)
    self.labl1.grid(row=0,column = 0, sticky ="NSW", padx = 5, pady = 5)    
    self.Entry1.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 5)
    self.submit.grid(row=2,column = 0, sticky ="NSW", padx = 5, pady = 5)
    pass


  

    

  def DoCert(self):
    self.id = (self.Entry1.get()).strip()
    
    print(self.diccionario)
    try:
      yx=int (self.id)
      
      
      
      if not(self.id in self.diccionario) :
        (self.labl2).grid_forget()
      
        self.labl3.grid(row=4,column = 0, sticky ="NSW", padx = 5, pady = 5)
      else:
        (self.labl3).grid_forget()
        self.labl2.grid(row=4,column = 0, sticky ="NSW", padx = 5, pady = 5)
        People_set = people("personalData")
        People_set.Mycertificate(self.id)
        print(self.id+" yes")
        #print("\n\nPorfavor dirijase a la carpeta de origen del programa, \nen ella encontrara un archivo llamado certificate.txt  "
      
    except:
      self.Entry1.delete(0,'end')
      self.Entry1.insert(0,"Ingrese un numero valido")
      pass