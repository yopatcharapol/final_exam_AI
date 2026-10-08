class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Example usage
person1 = Person("Sala Khunnawut", 61)

print("Initial Information:")
person1.display_info()

person2 = Person()
person2.set_name("ต่าย อรทัย")
person2.set_age(43)

person2.display_info()

person3 = Person(61)
person3.display_info()
