"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    # Class variable
    category = "General"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_info(self):
        """Return information about the object."""
        return f"Name: {self.name}, Age: {self.age}, Category: {self.category}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):

    # Class variable
    department = "Computer Science"

    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        return (
            f"Name: {self.name}, Age: {self.age}, "
            f"ID: {self.student_id}, Course: {self.course}, "
            f"Department: {self.department}"
        )

    def introduce(self):
        return f"I am {self.name}, studying {self.course}."

    # Student-created extension: update the student's course
    def update_course(self, new_course):
        self.course = new_course
        return f"{self.name} is now studying {self.course}."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.


def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # Create two ChildClass objects
    child1 = ChildClass("Unegbu", 22, "S1001", "Cybersecurity")
    child2 = ChildClass("Jordan", 24, "S1002", "Data Structures")

    # Access the class variable through the class
    print("Class variable:", ChildClass.department)

    # Access the same class variable through an object
    print("Object class variable:", child1.department)

    # Add an attribute to only one object
    child1.specialization = "Network Security"

    # Display each object's instance namespace
    print("Child1 namespace:", child1.__dict__)
    print("Child2 namespace:", child2.__dict__)

    # Display the class namespace information
    print("Class namespace:", ChildClass.__dict__)



# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # Create an object containing nested mutable data
    original = {
        "name": "Unegbu",
        "courses": ["Python", "Data Structures"]
    }

    # Create a shallow copy and a deep copy
    shallow_copy = copy(original)
    deep_copy = deepcopy(original)

    # Modify the original object's nested list
    original["courses"].append("Cybersecurity")

    # Display all three objects
    print("Original object:", original)
    print("Shallow copy:", shallow_copy)
    print("Deep copy:", deep_copy)

    # Shallow copies share references to nested objects.
    # Therefore, the shallow copy reflects the list modification.
    # Deep copies create independent nested objects.
    # Therefore, the deep copy retains its original course list.



# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    # Create and test a parent object
    print("\n=== Parent Object ===")
    parent = ParentClass("Unegbu", 25)
    print(parent.display_info())

    # Create and test a child object
    print("\n=== Child Object ===")
    child = ChildClass("Jordan", 22, "S1001", "Cybersecurity")
    print(child.display_info())
    print(child.introduce())

    # Student-created extension
    print(child.update_course("Cloud Security"))
    print(child.display_info())

    # Demonstrate class and instance namespaces
    demonstrate_namespaces()

    # Demonstrate shallow and deep copying
    demonstrate_copying()


if __name__ == "__main__":
    main()

