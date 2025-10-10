# To create bank account class
class bank:
    def __init__(self):
        self.bal=0 #Initialize balance 0
        print("Welcome to Honey BANK")
    def dep(self):
        amount=float(input("Nuvu yanth veyali anukuntunavu: "))
        self.bal += amount
        print("\nNuvu veysina amount:",amount)

    def withdraw(self):
        amount=float(input("Nuvu yantha teyali anukuntunavu:"))
        if self.bal>=amount:
            self.bal-=amount
            print("\nNuvu tesukuna amount:",amount)
        else:
            print("/nInsufficient balance")
    def display(self):
        print("\nNee account lo vunna motham money eppudu nuvu chusuko =",self.bal)


s = bank()

s.dep()
s.withdraw()
s.display()
