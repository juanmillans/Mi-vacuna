from Data.Text_processor import people
import datetime
from matplotlib import pyplot as plt

class CPU():

  def __init__(self, path):
    self.un = people("personalData")

    self.Data = people(path)  # List of person objects
    self.Population = (self.Data).CleanData()  #it should display a list of  10 person objects
    self.registered_ppl = (self.Data).RegisteredId

  def Ammount_of_vaccines(self, Y1, M1, Y2, M2):  # FUncion que recibe com input( en consola ) el ano 1 y mes 1 y ano dos y mes 2 , los cuales dan un rango de tiempo para el cual se retorna la cantidad de vacunas en ese rango.
    #interface = UI()
    #Y1 = interface.input_Ammoutofvaccines()

    initial_date = datetime.date(Y1, M1, 1)
    final_date = datetime.date(Y2, M2, 1)

    count = 0
    applied_doses = []
    for individual in self.Population:
      for vaccine in individual.vaccines:
        if (vaccine.ADate > initial_date) and (vaccine.ADate < final_date):
          applied_doses += [vaccine]

    return (len(applied_doses))

  def Vaccines_per_month(self, Y):
    # Esta funcion recibe como input (en consola) el ano Y y da como output una grafica de barras en la cual se muestra la cantidad de vacunas aplicadas por mes.

    M1 = 1
    M2 = 2
    VPM = []
    Cmonth = []
    initial_date = datetime.date(Y, M1, 1)
    final_date = datetime.date(Y, M2, 1)

    for month in range(0, 12):

      initial_date = datetime.date(Y, M1, 1)
      if M2 > 12:
        M2 = 1
        final_date = datetime.date(Y + 1, M2, 1)
      else:
        final_date = datetime.date(Y, M2, 1)
      applied_doses = []
      for individual in self.Population:
        for vaccine in individual.vaccines:
          if (vaccine.ADate >= initial_date) and (vaccine.ADate < final_date):
            applied_doses += [vaccine]
      VPM.append(len(applied_doses))
      m = (datetime.datetime.strptime(str(M1), "%m")).strftime("%b")
      Cmonth += [m]
      M1 += 1
      M2 += 1
    #print(VPM)
    #print(Cmonth)

    plt.bar(Cmonth, VPM)
    plt.title(Y)
    plt.xlabel("Meses")
    plt.ylabel("Vacunas administradas")
    plt.show()

  def V_AgeRange(self, Age0, Age1):
    # Esta funcion recibe como input( en consola ) un rango de edad que varia desde Age0 hasta Age 1

    counter = 0
    for individual in self.Population:
      if (individual.Age() >= Age0) and (individual.Age() <= Age1):
        counter += 1
    return (counter)

  def V_AgeDecade(self, num):
    # Esta funcion recibe un numero( en consola ) de 0- 13 que hace referencia a las edades  de 0-10, 10-20, 20-30,.........., y 130-140. suponiendo que el maximo que vive un ser humano son 14o anos. y da como output una lista que tiene como key una decada y como value tiene el numero de personas vacunadas en ese rango de edad.

    num = num * 10

    counter = 0
    Age0 = 0
    #decade_l ={"10":[],"20":[],"30":[],"40":[],"50":[],"60":[],"70":[],"80":[],"90":[],"100":[],"120":[],"130":[],"140":[]}
    decade_l = {}
    for decade in range(0, 14):

      for individual in self.Population:
        if (individual.Age() >= Age0) and (individual.Age() < Age0 + 10):
          counter += 1
      decade_l[f"{Age0}-{ Age0+10 }"] = counter
      Age0 += 10
      counter = 0

    return (decade_l[f"{num}-{ num+10 }"])

  def Vperperson_pie(self):
    # Esta graica de tortas no recibe ninguna clase de input, unicamente da output las vacunas por persona en una grafica.
    qtty = 0
    qtty_L = [0, 0, 0]
    E_qtty = ["one vaccine", "two vaccines", "three vaccines"]
    for guy in self.Population:
      qtty = len(guy.vaccines)
      if qtty == 1:
        qtty_L[0] += 1
      elif qtty == 2:
        qtty_L[1] += 1
      elif qtty == 3:
        qtty_L[2] += 1
      elif qtty == 4:
        qtty_L[3] += 1
      #elif qtty == 4:
        #qtty_L[4] += 1
      #elif qtty == 5:
        #qtty_L[5] += 1
      #elif qtty == 6:
        #qtty_L[6] += 1

    plt.pie(qtty_L,labels=E_qtty,wedgeprops={"edgecolor": "black"},autopct="%1.1f%%")

    plt.show(block=False)

  def Vperperson(self, num):
    # toma como input num que se refiere el numero de vacunas que que tiene una persona  y las pone en una lista que clasifica segun su indice la cantida de vacunas ( es decir 0,1,2,3....,6 )
    qtty = 0
    persons = 0
    answer = ""
    qtty_L = [0, 0, 0, 0, 0, 0, 0]
    for guy in self.Population:
      qtty = len(guy.vaccines)
      if qtty == 0:
        qtty_L[0] += 1
      elif qtty == 1:
        qtty_L[1] += 1
      elif qtty == 2:
        qtty_L[2] += 1
      elif qtty == 3:
        qtty_L[3] += 1
      elif qtty == 4:
        qtty_L[4] += 1
      elif qtty == 5:
        qtty_L[5] += 1
      elif qtty == 6:
        qtty_L[6] += 1
    if num < len(qtty_L):
      persons = qtty_L[num]
      answer = f"Hay {persons} personas registradas que se aplicaron {num} vacunas "
    else:
      persons = qtty_L[-1]
      answer = f"El numero maximo de vacunas posible\n por personas es de {6} vacunas y hay {persons} \n personas vacunadas con esta cantidad. "

    return (answer)

  def certificate(self, ID):
    # toma como imput el Id que es el numero de identificacion del sujeto y da ouput un txt en que se registra el certificado de vacunacion  con sus vacunas, el numero de lote mas cosas.
    myself = people("personalData")
    myself.Mycertificate(str(ID))

  def registeredppl(self):
   
    return((self.un).RegisteredId())
