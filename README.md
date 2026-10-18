# unit1-python-oop
Python OOP assignment demonstrating inheritance, namespaces, and shallow and deep copying.
Unit 1 Discussion: Python OOP, Namespaces, and Copying
Overview
This project is to illustrate the concepts of Object-Oriented Programming (OOP) in Python to the student, such as inheritance, class and instance namespaces, shallow copying and deep copying.
Learning Objectives
•	Create parent and child classes.
•	Extend functionality using inheritance.
•	Know how to use class and instance namespaces.
•	Demonstrate shallow and deep copying.
•	Use object-oriented design concepts.
Implementation Summary
ParentClass
Shared object information, such as name and age are specified in the parent class. It also contains a category class variable and a way to print out information about the objects.
ChildClass
ChildClass inherits from ParentClass and calls super() to set up inherited attributes. It introduces department class variable, student_id and student attributes, and displays student information, as well as introduces student.
Namespaces
The showChildren method creates two instances of the Namespace demo and prints their instance attributes and class attributes. It also illustrates the ability of an attribute added to an object to be unique to that object.
Shallow Copying and Deep Copying.
The copying demonstration is based on a dictionary that contains a nested list of courses. It demonstrates deep copy and shallow copy and differentiates the impact of changing nested data on the copies.
Student-Created Extension
A student's course can be changed in the update_course() method. In this program, the feature is tested when the Course to the course icon is updated from Cybersecurity to Cloud Security, and the new information is displayed.
Practical Application
These ideas can be used in student management systems and elsewhere in applications where one would like to be able to reuse classes, organize attributes and manage copied data.
How to Run
•	open the file unit1_discussion.py in IntelliJ IDEA.
•	Choose the interpreter (python) you have configured.
•	Run the file.
•	Look at the console output for the parent and child objects, the namespace demonstration and copying demonstration.
Technologies
•	Python
•	IntelliJ IDEA
•	Python copy module
