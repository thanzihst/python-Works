class Grandparent:
    def m1(self):

        print("Grand parnt method")

class Parent:
    def m2(self):

        print("parent method")


class child(Parent,Grandparent):
    def m3(self):


        print("child class method")


childinstance=child()

childinstance.m3()
childinstance.m2()
childinstance.m1()
    