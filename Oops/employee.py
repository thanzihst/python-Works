class persion:



    def __init__(self,age,name,gender):

        self.age=age
        self.name=name
        self.gender=gender

    def display(self):

        print(self.age,self.name,self.gender)



class Employee(persion):

    def __init__(self, age, name, gender,eid,department,salary):
        super().__init__(age, name, gender)

        self.eid=eid
        self.department=department
        self.salary=salary

    def display(self):
        super().display()
        print(self.eid,self.department,self.salary)



Employeeinst=Employee("vpin",643,"male","hr",56748,878988)
Employeeinst.display()