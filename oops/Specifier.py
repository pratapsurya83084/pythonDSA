class Student:
    def __init__(self, name, age):
        self._name=name;
        self._age = age;   # protected

s = Student("Pratap", 21)
print(s._age)   # ⚠️ Technically accessible, but should be avoided
print(s._name.lower())   # pratap
print(s._name.upper())   # PRATAP

