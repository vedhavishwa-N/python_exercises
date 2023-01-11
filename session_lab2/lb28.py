"""Write a function to find out the professional tax applicable for an employee when salary is provided. 
The professional tax is to be computed at 0.25% of the salary amount. 
If the salary is less than 10000, professional tax applicable will be zero
"""
def professional_tax_finder (employee_salary):
    if employee_salary < 10000:
        professional_tax = 0
    else:
        professional_tax = employee_salary * 0.25
    return professional_tax

#test case
 
print ("the professional tax for salary of {} is {}".format (10000, professional_tax_finder (20000)))
print ("the professional tax for salary of {} is {}".format (9999, professional_tax_finder (9999)))

