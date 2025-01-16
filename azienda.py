class Employee:
    def __init__(self, name, h_pay):
        self.name = name
        self.h_pay = h_pay

    def tredi(self):
        return (self.h_pay *8 * 20) * 0.8

    def calc_wage(self):
        print(f"RAL di {self.name}")
        ral = self.h_pay * 8 * 20 * 12 + self.tredi()
        return ral


class Manager(Employee):
    yearly_bonus = 20
    def __init__(self, name, h_pay, division):
        super().__init__(name, h_pay)
        self.division = division

    def calc_wage(self):
        # Calcolo del RAL con il bonus annuale
        print(f"RAL di {self.name} con bonus")
        ral = self.h_pay * 8 * 20 * 12 + self.tredi() + self.yearly_bonus
        return ral


class Clerk(Employee):
    def __init__(self, name, h_pay, boss):
        self.boss = boss
        super().__init__(name, h_pay)


class Intern(Clerk):
    forfait = 500
    # override del metodo calc_wage()
    def __init__(self, name, boss):
        super().__init__(name, 0, boss)

    def calc_wage(self):
        print(f"{self.name} prende {self.forfait} € al mese")
        print(f"RAL di {self.name}")
        ral = self.forfait * 12
        return ral


obj1 = Manager("Elon Musk", 50, "Marketing")
obj2 = Clerk("Pippo", 35, obj1)
obj3 = Intern("Povero Tapino", obj1)

print(obj1.calc_wage())
print(obj2.calc_wage())
print(obj3.calc_wage())