#  File: Employee.py
#  Student Name: Natalia Ortega Arriaga
#  Student UT EID: NO4432

class Employee:
    def __init__(self, **kwargs):
        self._employee_name = kwargs.get('name')
        self._employee_id = kwargs.get('id')
        self._base_salary = kwargs.get('salary')

    @property
    def name(self):
        return self._employee_name

    @property
    def id(self):
        return self._employee_id

    @property
    def salary(self):
        return self._base_salary

    @salary.setter
    def salary(self, value):
        self._base_salary = value

    def __str__(self):
        return f"Employee\n{self.name}, {self.id}, {self.salary}"


class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._added_benefits = kwargs.get('benefits', [])

    # Additional benefits impact salary
    def cal_salary(self):
        base = self.salary
        if "health_insurance" in self._added_benefits and "retirement" in self._added_benefits:
            return base * 0.7
        elif "health_insurance" in self._added_benefits:
            return base * 0.9
        elif "retirement" in self._added_benefits:
            return base * 0.8
        else:
            return base

    @property
    def benefits(self):
        return self._added_benefits

    @benefits.setter
    def benefits(self, benefit_list):
        self._added_benefits = benefit_list

    def __str__(self):
        return f"Permanent_Employee\n{self.name}, {self.id}, {self.salary}, {self.benefits}"


class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._bonus_amount = kwargs.get('bonus', 0)

    def cal_salary(self):
        return self.salary + self._bonus_amount

    @property
    def bonus(self):
        return self._bonus_amount

    @bonus.setter
    def bonus(self, bonus_value):
        self._bonus_amount = bonus_value

    def __str__(self):
        return f"Manager\n{self.name}, {self.id}, {self.salary}, {self.bonus}"


class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._hours_worked = kwargs.get('hours', 0)

    def cal_salary(self):
        return self.salary * self._hours_worked

    @property
    def hours(self):
        return self._hours_worked

    @hours.setter
    def hours(self, hours_value):
        self._hours_worked = hours_value

    def __str__(self):
        return f"Temporary_Employee\n{self.name}, {self.id}, {self.salary}, {self.hours}"


class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._trips = kwargs.get('travel', 0)  # Changed '_num_trips' to '_trips'

    def cal_salary(self):
        temp_salary = super().cal_salary()
        trip_cost = self._trips * 1000  # Changed '_num_trips' to '_trips'
        return temp_salary + trip_cost

    def __str__(self):
        return f"{super().__str__()}, {self._trips}"  # Changed '_num_trips' to '_trips'



class Consultant_Manager(Consultant, Manager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._manager_bonus = kwargs.get('bonus', 0)

    def cal_salary(self):
        consult_pay = Consultant.cal_salary(self)
        return consult_pay + self._manager_bonus

    def __str__(self):
        return f"{super().__str__()}, {self._manager_bonus}"


''' ##### DRIVER CODE #####
    ##### Do not change. '''


def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()


