# 1. Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))


class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
    def assign_department(self,change_emp_department):
        self.emp_department = new_department
    def print_employee_details(self,emp_obj):
        print(emp_obj)
    def calculate_emp_salary(self,salary,overtime):
        if overtime>50:
            overtime_amount=overtime*self.salary/50
            return salary+overtime_amount
        return salary



emp1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2=Employee("JONES", "E7499", 45000, "RESEARCH")
emp3=Employee("MARTIN", "E7900", 50000, "SALES")
emp4=Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp=[emp1,emp2,emp3,emp4]

for i in emp:
    i.




#2  Write a Python class Restaurant with attributes like menu_items, book_table, and 
# customer_orders, and methods like add_item_to_menu, book_tables, and customer_order.
# Perform the following tasks now:
# Now add items to the menu.
# Make table reservations.
# Take customer orders.
# Print the menu.
# Print table reservations.
# Print customer orders.

class Restaurent:
    def __init__(self,menu_items, book_table, customer_orders):
        self.menu_items=menu_items
        self.book_table=book_table
        self.customer_orders=customer_orders
    
    def add_item_to_menu(self,new_items):
        self.menu_items.append(new_items)
    
    def book_tables(self,table_no,cust_name):
        self.book_table[table_no]=cust_name
    
    def customer_order(self,item):
        self.customer_orders=[menu_items[i] for i in range(len(menu_items)) if item in menu_items[i]]
    
menu_items=["dosa","idly","Bonda"]
book_table={1:"Pranay"}
customer_orders=[]

restaurent=Restaurent(menu_items,book_table,customer_orders)

restaurent.add_item_to_menu("puri")
restaurent.book_tables(2,"UDN")
restaurent.customer_order("dosa")
restaurent.menu_items
restaurent.book_table
restaurent.customer_orders
