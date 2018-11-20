'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''



def divisor(number):
    range_of_numbers = int(input('Enter range of numbers to test divisibility: '))
    print("According to the range 1 - {}, {} can only be divided by: ".format(range_of_numbers, number))
    for i in range(1,range_of_numbers):
        if number % i == 0:
            print(i)


if __name__ == '__main__':
    number = int(input('Enter Number: '))
    divisor(number)