"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
yearsleft = 100 - age
currentyear = 2019
resultyear = currentyear + yearsleft
print(name , "will be 100 years old in the year" , resultyear)
