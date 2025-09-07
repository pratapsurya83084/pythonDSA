

# class Student:
#     name="pratap"


# s1 =  Student()
# print(s1.name)  # Output: pratap

# s1.name="karan"

# print(s1.name)  # Output: karan
# print(Student.name)  # Output: pratap


# constructor


class Animal:
    name=""
    color=""

# ddefault constructor  - there is no argument or parameter
def __init__(self):
      print("this is default constructor")

def __init__(self ,name,color):
        self.name=name
        self.color=color

a1 = Animal("elephant","grey")
print(a1.name)        
print(a1.color)        











