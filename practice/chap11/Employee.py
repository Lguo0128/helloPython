class Employee:
    def __init__(self, firstname, lastname, annual_salary):
        """接受名、姓和年薪，并将它们都存储在属性中"""
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = int(annual_salary)

    def give_raise(self, raise_mount=""):
        if raise_mount:
            self.annual_salary = self.annual_salary + int(raise_mount)
        else:
            self.annual_salary += 5000
