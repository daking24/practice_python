'''
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''


universal_list = [3,4,5,7,89,2,1,0]
list_less_than_5 = []


for i in universal_list:
    if i < 5:
        list_less_than_5.append(i)

print(list_less_than_5)
