# Variable Assignment
# variable can not start with number or special characters

print("Variable Assignment: ")
x = 2
print("x is {} ".format(x))

# String
print("String:")
my_str = 'my string'
my_str2 = "what's this?"
print(my_str)
print(my_str2)

# printing
num = 5
name = "Fan"
print('My number is: {one}, and my name is {two}'.format(one=num, two=name))
print('My number is: {}, and my name is {}'.format(num, name))

# Lists
my_list = ['a', 'b', 'c', 'd']
my_list.append('e')
print(my_list)
my_list[0] = 'new'
print(my_list)
nest_list = [1, 2, 3, [3, 5, ['target']]]
print(nest_list[3][2][0])

# Dictionaries
my_dic = {'k1': 'val1', 'k2': 'val2'}
print(my_dic['k1'])
# Tuple, tuple is immutable
my_tup = (1, 2, 3, 4)
a, b, c, d = my_tup
print(my_tup)
print(c)


# functions
def my_func(param1='default'):
    """
         Dosstring goes here
     """
    print(param1)


my_func()
my_func('new param')

z = lambda val='default': val
print(z())
print(z('thanks'))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# methods
my_string = 'Welcome to PyCharm course'
print(my_string.lower())
print(my_string.upper())
print(my_string.split())

ans = (lambda x, y: x * y)(9, 10)
print(ans)

# Sorting a List by the last name using lambda expression
presidents_sg = ["Yusof Ishak", "Benjamin Sheares", "Devan Nair", "Wee Kim Wee", "Ong Teng Cheong", "Sellappan Nathan",
                 "Tony Tan", "Halimah Yacob"]
presidents_sg.sort(key=lambda name: name.split(" ")[-1].lower())
print(presidents_sg)

nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(' '.join(map(str, square_all)))

for i in square_all:
    print(i)


def volume(a):
    """volumne of a cube with edge 'a'"""
    return a ** 3


# Edge, say length in cm
edges = [1, 2, 3, 4, 5]
# calculate and print answers
print(list(map(volume, edges)))

# Convert height from cms to feet : 1 cm = 0.0328 feet
height_in_cms = [('Po Ping', 183), ('Oogway', 161), ('Shifu', 130), ('Tigress', 179), ('Viper', 190), ('Monkey', 165),
                 ('Crane', 165), ('Mantis', 45)]
convertToFeet = lambda cm: (cm[0], round(cm[1] * 0.0328))
print(list(map(convertToFeet, height_in_cms)))

# Filter out all the numbers greater than 4 from a list
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output_list = filter(lambda x: x > 4, some_list)
print(list(output_list))

# Removing missing values from a list
countries_asia = ["Bhutan", "", "", "China", "Myanmar", "", "India", "Indonesia", "", "Philippines", "Singapore"]
print(list(filter(None, countries_asia)))

# importing functools for reduce()
import functools

# Compute the product of a list of integers using
# 'reduce'function from functools import reduce
product = functools.reduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
print(product)

# Determining the maximum number in a given list
from functools import reduce

f = lambda a, b: a if (a > b) else b
print(reduce(f, [58, 698, 12, 158, 6, 79, 82]))

