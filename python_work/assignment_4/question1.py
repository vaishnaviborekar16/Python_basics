#WAP to get details of the EMP and print/display for 5 employees take userinput for values

class Employee_Detail:
    def __init__(self,id,name,salary):
        self.Id=id
        self.Name=name
        self.Salary=salary

    def setValue(self):
        self.Id=input("Enter id of employee : ")
        self.Name=input("Enter employee name: ")
        self.Salary=float(input("Enter salary: "))

    def disp(self):
        print("Employee Details are")
        print(self.Id)
        print(self.Name)
        print(self.Salary)
e=[]
for i in range(5):
    name=input("Name: ")
    id=int(input("ID: "))
    salary=int(input("Salary:"))
    objEmp=Employee_Detail(name,id,salary)
    e.append(objEmp)

for i in range(5):
    e[i].disp()

           
