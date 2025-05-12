class Employee:
    def __init__(self,staff_id,name,age,address,salary):
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary

#    def validation(self):
 #       if (str(self.staff_id) == "39" and self.name == "Muazu"):
  #          print("This is Muazu and his age is:",self.age, ", His address is:", self.address, "And his salary is:", self.salary)
   #     else:
    #        print("Not Muazu")    

#x = Employee(39,"Muazu",20,"lokogoma",200000)
#x.validation()


#INHERITANCE
class Child(Employee):
    def __init__(self, staff_id, name, age, address, salary, role, department, yoe):
        super().__init__(staff_id, name, age, address, salary)
        self.yoe = yoe
        self.role = role
        self.department = department

    def child_info(self):
        print("Additional employee information:",self.role, "Employee department:",self.department, "and year of experience:",self.yoe)    
x = Child(39,"Muazu",20,"lokogoma",200000,"Quality assurance","IT",2)
x.child_info()


#
try:
    a = 5
    b = "Muazu"
    c = a/b
    print("This is the value of ",c)
except SyntaxError:
    print("This is a syntax error")
except TypeError:
    print("This is a type error")
finally:
    print("This is a python error try example")
    
import time
q = time.localtime()
r = time.strftime("%D:%M:%Y,%H:%M:%S",q)
print("localtime",q)
print(r)