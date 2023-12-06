"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class SalaryEmployee(Employee):
    def __init__(self, name, monthlySalary):
        super().__init__(name)
        self.monthlySalary = monthlySalary
    
    def get_pay(self):
        return self.monthlySalary
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthlySalary}. Their total pay is {self.get_pay()}."
    
class HourlyEmployee(Employee):
    def __init__(self, name, hourlyRate, hours):
        super().__init__(name)
        self.hourlyRate = hourlyRate
        self.hours = hours
    
    def get_pay(self):
        return self.hourlyRate * self.hours
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyRate}/hour. Their total pay is {self.get_pay()}."

class SalaryEmployeeWithBonus(SalaryEmployee):
    def __init__(self, name, monthlySalary, bonus):
        super().__init__(name, monthlySalary)
        self.bonus = bonus
    
    def get_pay(self):
        return super().get_pay() + self.bonus
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."

class HourlyEmployeeWithBonus(HourlyEmployee):
    def __init__(self, name, hourlyRate, hours, bonus):
        super().__init__(name, hourlyRate, hours)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyRate}/hour and receives a bonus commission of {self.bonus}. Their total pay is {self.get_pay()}."
    
class SalaryEmployeeWithContractCommission(SalaryEmployee):
    def __init__(self, name, monthlySalary, contracts, commission):
        super().__init__(name, monthlySalary)
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + (self.contracts * self.commission)
    
    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."

class HourlyEmployeeWithContractComission(HourlyEmployee):
    def __init__(self, name, hourlyRate, hours, contracts, commission):
        super().__init__(name, hourlyRate, hours)
        self.contracts = contracts
        self.commission = commission

    def get_pay(self):
        return super().get_pay() + (self.contracts * self.commission)
    
    def __str__(self):
        return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyRate}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract. Their total pay is {self.get_pay()}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployeeWithContractCommission('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployeeWithContractComission('Jan', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployeeWithBonus('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployeeWithBonus('Ariel', 30, 120, 600)
