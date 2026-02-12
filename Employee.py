class Employee:
    hra_percentage = 20 

    def __init__(self, emp_id, name, salary, leave_days):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.leave_days = leave_days
    def calculate_salary(self):
        hra = (Employee.hra_percentage / 100) * self.salary
        return self.salary + hra
    def apply_leave_deduction(self):
        per_day_salary = self.salary / 30
        return self.leave_days * per_day_salary
    def display_payslip(self):
        gross_salary = self.calculate_salary()
        deduction = self.apply_leave_deduction()
        net_salary = gross_salary - deduction

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("HRA %:", Employee.hra_percentage)
        print("Leave Days:", self.leave_days)
        print("Net Salary:", net_salary)
    @classmethod
    def update_hra_percentage(cls, new_hra):
        cls.hra_percentage = new_hra
emp1 = Employee(101, "Uma", 50000, 2)
emp1.display_payslip()
Employee.update_hra_percentage(25) 
emp1.display_payslip()
