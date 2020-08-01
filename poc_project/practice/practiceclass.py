
class Employee:
    no_of_employees = 0
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'.'+'@cybage.com'
        Employee.no_of_employees += 1


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_reaise(self):
        self.pay = int(self.pay* self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str ):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt = 10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employee = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print(emp.fullname())

dev1 = Developer("Kunal", 'Sable', 200000, 'Java')
dev2 = Developer('Mohan', "Singh", 30000, 'Python')

mgr1 = Manager('Ravi', 'sharma', 30000, [dev1])

mgr1.add_employee(dev2)
mgr1.remove_employee(dev1)

mgr1.print_employee()

#
# print(dev1.first)
# print(dev1.fullname())

#print(help(Developer))

#
# emp1 = Employee("Ravi", 'Sharma', 200000)
# emp2 = Employee('Mohan', "Singh", 30000)



# import datetime
#
# my_date = datetime.date(2020,7,8)
# print(Employee.work_day(my_date))
# ravindra = Employee.from_string("Ravindra'-Sharma-90000")
#
# print(ravindra.first)
#print('{} {}'.format(emp1.first , emp1.last))
#emp2 = Employee()
# print(emp1.first)
#emp1.raise_amt = 1.05
#print(dir(emp1))
#print(emp1.__repr__())
# Employee.set_raise_amt(1.06)
# emp1.set_raise_amt(1.05)
# print(emp1.raise_amt)
# print(emp2.raise_amt)
# print(Employee.raise_amt)


# print(emp1.raise_amt)
# print(emp1.fullname())
# print(Employee.fullname(emp1))



