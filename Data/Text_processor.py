from Data.person import person
from Data.vacuna import vacuna


class people():

  def __init__(self, Path):
    self.Path = Path
    self.PData = open(f"Data/{self.Path}.txt",
                      "r")  #  PData is short for personal data
    self.rows = self.PData.readlines()  #personal data is to be stored in rows
    #print( last_line)
    self.r_index = 0  # initializing row index and current row in the text
    self.C_row = [
    ]  # current row is a list of different values separated by commas
    self.last_row = self.rows[-1].split(
      ",")  # last item of all items in the list
    self.Plist = []  # list of person objects with all their information

  def CleanData(self):

    while self.C_row != self.last_row:

      if self.r_index == len(
          self.rows):  #  if we surpassed the maximum row index
        break
      else:  # otherwise
        self.C_row = (self.rows[self.r_index]).split(
          ",")  # move to the next row

      if "cc" == self.C_row[0] or "ti" == self.C_row[
          0]:  # if the beginning of the current row has a cc item on it's beginign
        p = person(
          self.C_row
        )  # we assing a person p with the C_row to proccess it, to make it a record.

        self.r_index += 1  #Then we move on
        self.C_row = (self.rows[self.r_index]).split(",")  # to the next row

        while self.C_row != [
            '\n'
        ]:  # so long as the current row is not an empty space
          v = vacuna(self.C_row)  # we assing the row to a vaccine object

          (p.vaccines).append(
            v
          )  # we append the vaccine to a persons atribute of vaccines which is a list.

          self.r_index += 1  #Then we move on to the next row

          if self.r_index == len(
              self.rows):  
            break
          else:  # otherwise
            self.C_row = (self.rows[self.r_index]).split(
              ",")  # move to the next row
        self.r_index += 1  #  when we finished with that guy we skip the empty space "\n"
        self.Plist.append(p)
    return (self.Plist)

  def Mycertificate(self, cc):
    outputCertificate = open("Certificate/certificate.txt", "w")
    flag = ""

    while self.C_row != self.last_row:

      self.C_row = (self.rows[self.r_index]).split(",")

      if ("cc" == self.C_row[0]
          or "ti" == self.C_row[0]) and (cc == self.C_row[1].strip()):
        flag = "up"
        for items in self.C_row:
          outputCertificate.write(items + " ")
        outputCertificate.write("\n")

        self.r_index += 1
        self.C_row = (self.rows[self.r_index]).split(",")

        while self.C_row != ['\n']:
          for items in self.C_row:
            outputCertificate.write(items)
          outputCertificate.write("\n")

          self.r_index += 1
          if self.r_index == len(self.rows):
            break
          else:
            self.C_row = (self.rows[self.r_index]).split(",")

        self.r_index += 1
      if self.r_index >= len(self.rows):
        break
      else:
        self.C_row = (self.rows[self.r_index]).split(",")

      if (self.C_row == ["\n"] and flag == "up"):
        break

      self.r_index += 1

    outputCertificate.close()

  def RegisteredId(self):
    registered_People = {}

    flag = ""

    while self.C_row != self.last_row:

      self.C_row = (self.rows[self.r_index]).split(",")

      if ("cc" == self.C_row[0] or "ti" == self.C_row[0]):

        registered_People[str(self.C_row[1])] = f'{str(self.C_row[2])+" "+str(self.C_row[3])}'

      if self.r_index >= len(self.rows):
        break
      else:
        self.C_row = (self.rows[self.r_index]).split(",")

      if (self.C_row == ["\n"] and flag == "up"):
        break

      self.r_index += 1
    #print(registered_People)
    return (registered_People)
