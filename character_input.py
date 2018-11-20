'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

'''


name = input("Enter your name: ")
age = int(input("Enter your age: "))
year_born = 2018 - age
year_to_bo_100 = year_born + 100


print("Hello ", name, 'You will be 100 in the year', year_to_bo_100)
