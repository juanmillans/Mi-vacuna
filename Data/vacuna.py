from datetime import date

class vacuna():
    def __init__(self,record):
        items = record
        self.ADate = date.fromisoformat(items[0].strip())
        self.brand = items[1].strip()
        self.lot = items[2].strip()
        self.vaccinationCenter = items[3].strip()
        self.vaccinator= items[4].strip()
    
