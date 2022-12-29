import tkinter as tk


# deathwing=Image.open('Deathwing.PNG')
# image2=deathwing.resize((100,50),Image.ANTIALIAS)
#Deathwing2=ImageTk.PhotoImage(image2)



class Home:
  def  __init__(self,p_windw):
    self.methodsframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5)
    self.descriptionframe=tk.LabelFrame(master=p_windw,
                              padx=5,
                              pady=5,bg="#70CBFF")
    self.labl0 = tk.Label(master=self.descriptionframe,
                     text = "Para mostrar la opcion deseada presione el numero que se encuentra\nal lado de la opcion deseada ",
                     padx = 1, pady = 1,justify="left",bg="#70CBFF")   

    self.labl1 = tk.Label(master=self.methodsframe,
                     text = "1) Vacunación en un rango de edad",
                     padx = 1, pady = 1,justify="left")
    self.labl2 = tk.Label(master=self.methodsframe,
                     text = "2) Cantidad de vacunas aplicadas en un rango de tiempo",
                     padx = 1, pady = 1,justify="left")
    self.labl3 = tk.Label(master=self.methodsframe,
                     text = "3) Grafico de barras de las vacunas aplicadas en un año especifico",
                     padx = 1, pady = 1,justify="left")
    self.labl4 = tk.Label(master=self.methodsframe,
                     text = "4) Grafico de torta con la cantidad de vacunas aplicadas por persona",
                     padx = 1, pady = 1,justify="left")
    self.labl5 = tk.Label(master=self.methodsframe,
                     text = "5) Grafico de torta con la cantidad de vacunas aplicadas por persona",
                     padx = 1, pady = 1,justify="left")
    self.labl6 = tk.Label(master=self.methodsframe,
                     text = "6) Obtener su certificado",
                     padx = 1, pady = 1,justify="left")
  def  show_all(self):
    self.labl0.grid(row=1,column = 0, sticky ="NSW", padx = 5, pady = 12)
    self.labl1.grid(row=2,column = 0, sticky ="NSW", padx = 5, pady = 12)
    self.labl2.grid(row=4,column = 0, sticky ="NSW", padx = 5, pady = 12) 
    self.labl3.grid(row=6,column = 0, sticky ="NSW", padx = 5, pady = 12)
    self.labl4.grid(row=8,column = 0, sticky ="NSW", padx = 5, pady = 12)
    self.labl5.grid(row=10,column = 0, sticky ="NSW", padx = 5, pady = 12)
    self.labl6.grid(row=12,column = 0, sticky ="NSW", padx = 5, pady = 12)