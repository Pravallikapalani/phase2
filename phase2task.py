# class student:
#     def __init__(self,name,rollno,python,java,DS,maths,C):
#         self.name=name
#         self.rollno=rollno
#         self.python=python
#         self.java=java
#         self.DS=DS
#         self.maths=maths
#         self.C=C
# obj=student("kavya",5,89,76,52,75,78)
# print(obj.name)
# print(obj.rollno)
# print(obj.python)
# print(obj.java)
# print(obj.DS)
# print(obj.maths)
# print(obj.C)

# obj=student("pravalli",21,85,79,69,81,72)
# print(obj.name)
# print(obj.rollno)
# print(obj.python)
# print(obj.java)
# print(obj.DS)
# print(obj.maths)
# print(obj.C)

# obj=student("sai",6,89,68,56,92,78)
# print(obj.name)
# print(obj.rollno)
# print(obj.python)
# print(obj.java)
# print(obj.DS)
# print(obj.maths)
# print(obj.C)

# obj=student("priya",25,78,58,69,85,88)
# print(obj.name)
# print(obj.rollno)
# print(obj.python)
# print(obj.java)
# print(obj.DS)
# print(obj.maths)
# print(obj.C)



class student:
    def __init__(self,name,rollno,python,java,DS,maths,C):
        self.name=name
        self.rollno=rollno
        self.python=python
        self.java=java
        self.DS=DS
        self.maths=maths
        self.C=C
    def printalldetails(self):
        print(self.name)
        print(self.rollno)
        print(self.python)
        print(self.java)
        print(self.DS)
        print(self.maths)
        print(self.C)
obj=student("kavya",5,89,76,52,75,78)
obj.printalldetails()
obj2=student("pravalli",21,85,79,69,81,72)
obj.printalldetails()
obj3=student("sai",6,89,68,56,92,78)
obj.printalldetails()
obj4=student("priya",25,78,58,69,85,88)
obj.printalldetails()
