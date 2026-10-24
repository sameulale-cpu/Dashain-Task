# Create a Python class named "Employee".

# Requirements:

# - Define attributes such as employee ID, name, department, and salary.
# - Use a constructor ("init") to initialize employee details.
# - Create methods to display employee information and calculate annual salary.
# - Create at least three employee objects and display their details.

class Employee:
    def __init__(self, employee_ID, name, department, salary):
        self.employee_ID = employee_ID
        self.name = name
        self.department = department
        self.salary = salary

    def details(self):
        print(f"""Employee ID: {self.employee_ID}
Name: {self.name}
Department: {self.department}
Salary: {self.salary}""")

    def annual_salary(self):
        return (self.salary * 12)

Employee1 = Employee(1, "Hari", 1, 1500)
Employee1.details()
print(f"Annual salary: {Employee1.annual_salary()}")

Employee2 = Employee(2, "Ram", 2, 2500)
Employee2.details()
print(f"Annual salary: {Employee2.annual_salary()}")

Employee3 = Employee(3, "Gita", 3, 3500)
Employee3.details()
print(f"Annual salary: {Employee3.annual_salary()}")
