import re

class Person:
    def __init__(self, name, age, emails):
        self.name = name
        self.age = age
        self.emails = emails

    def isValidToInclude(self):
        errors = []

        if len(self.name.split()) < 2:
            errors.append("Nome deve ter ao menos 2 partes")
        elif not self.name.replace(" ", "").isalpha():
            errors.append("Nome deve ser composto apenas por letras")

        if not 1 <= self.age <= 200:
            errors.append("Idade deve estar entre 1 e 200")

        if not self.emails:
            errors.append("Pessoa deve ter pelo menos um email associado")
        else:
            for email in self.emails:
                if not email.validateEmail():
                    errors.append("Formato de email inválido")

        return errors

class Email:
    def __init__(self, address):
        self.address = address

    def validateEmail(self):
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.address) is not None