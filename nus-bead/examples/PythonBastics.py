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



