# employee.py

class Employee:
    def __init__(self, name, email, salary, position):
        self.name = name
        self.email = email
        self.salary = salary
        self.position = position

    def calculate_net_salary(self):
        if self.position == "DESENVOLVEDOR":
            if self.salary >= 3000:
                return self.salary * 0.8
            else:
                return self.salary * 0.9
        elif self.position == "DBA" or self.position == "TESTADOR":
            if self.salary >= 2000:
                return self.salary * 0.75
            else:
                return self.salary * 0.85
        elif self.position == "GERENTE":
            if self.salary >= 5000:
                return self.salary * 0.7
            else:
                return self.salary * 0.8
        else:
            raise TypeError("Cargo inválido")