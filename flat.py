class Bill():

    def __init__(self, amount, period):
        self.amount = amount
        self.period=period

class Flatemate():

    def __init__(self, name , days_in_house):
        self.name=name
        self.days_in_house=days_in_house

    def pay(self, bill, flatmate):
        return bill.amount * (self.days_in_house / (self.days_in_house + flatmate.days_in_house))