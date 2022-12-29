from datetime import date
from dateutil import relativedelta

class person():
    def __init__(self,record):
        items=record
        self.idType = items[0].strip()
        self.id = items[1].strip("")
        self.lastname = items[2].strip()
        self.name = items[3].strip()
        self.birthDate = date.fromisoformat(items[4].strip())
        self.country = items[5].strip()
        self.vaccines=[]    
    def Age(self):
        age= relativedelta.relativedelta(date.today(), self.birthDate)
        age_in_years =age.years
        return(age_in_years)