

# # 1. Default Constructor
# # A constructor that has no parameters (except self).
# # It does not accept values from outside; it only initializes with default values.
# class Student:
#     def __init__(self):   # default constructor
#         self.name = "Unknown"
#         self.age = 0

#     def display(self):
#         print("Name:", self.name, "Age:", self.age)


# s1 = Student()
# s1.display()


# # 2. Parameterized Constructor
# # A constructor that takes parameters (other than self) to initialize object attributes.

# class Student:
#     def __init__(self, name, age):   # parameterized constructor
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name, "Age:", self.age)


# s1 = Student("Pratap", 21)
# s2 = Student("Amit", 22)

# s1.display()
# s2.display()



# # 3. Constructor with Default Arguments
# # A constructor where parameters have default values, so you can call it with or without arguments.
# class Student:
#     def __init__(self, name="Unknown", age=0):   # default arguments
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name, "Age:", self.age)


# s1 = Student()               # uses default values
# s2 = Student("Pratap", 21)   # uses given values

# s1.display()
# s2.display()





# default construcrtor

# class Animal:
#     def __init__ (self):
#      self.name="elephant is a default name"
#      self.color="grey is a default color"
#      print("this is a default constructor")
#     def display(self):
#        print("name of Animal is : " , self.name,"color of Animal is : " , self.color)
#     #    print()

# a1 = Animal()   

# a1.display()  # Output: 





# parameterized constructor
# class User:
#     def __init__ (self,username,password):
#         self.username = username;
#         self.password = password;

#     def display(self):
#         print("username is :",self.username,"password is :",self.password);    

# u1= User("pratap","123@#@1");
# u1.display();   # Output: username is : pratap password is : 123@#@1        

# parameerized default constructor

# class Car:
#     def __init__ (self,name="indica",color="blue"):
#         self.name=name;
#         self.color=color;
#     def display(self):
#         print("name of car is :",self.name,"color of car is :",self.color);

# c1 = Car();
# c1.display(); 


# take a name of student and 3 suject mark and print method to return avg or mark

class Student:
    name="";
    list=[];
    # constructor
    def __init__ (self,name,list):
        self.name = name;
        self.list = list;
    
    def avg(self):
        return sum(self.list)/len(self.list);

s1 = Student("pratap",[89,94,95]);
print("avg of student is :",s1.avg());
