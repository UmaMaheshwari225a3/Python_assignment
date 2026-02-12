class Patient:
    consultation_fee = 250
    daily_charge = 1000
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
        self.is_admitted = False
        self.is_discharged = False
    def admit(self):
        if not self.is_admitted:
            self.is_admitted = True
        print(f"{self.name} admitted successfully")

    def discharged(self):
        if self.is_admitted and not self.is_discharged:
            self.is_admitted = False
            self.is_discharged = True
            print(f"{self.name} discharged succesfully")
        else:
            print(f"{self.name} is not admitted or already discharged")
    def cal_bill(self, days):
        if self.is_admitted:
            total_bill = days*Patient.daily_charge + Patient.consultation_fee
            print(f"Total bill : {total_bill}")
    @classmethod
    def update_consultation_fee(cls, new_fee):
        cls.consultation_fee = new_fee
        print(f"Updated consultation fee : {new_fee}")

p1 = Patient("Uma", 20, "1234567890")
p1.admit()
p1.cal_bill(5)
p1.discharged()
p1.update_consultation_fee(300)

    
