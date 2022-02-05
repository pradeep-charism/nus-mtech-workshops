print("-" * 25, "Workshop 10 Start", "-" * 25)

# a) What is 8 to the power 4?
print(8 ** 4)
print("-" * 25)

# b) Split this string “Split this string”
print("Split this string".split(" "))
print("-" * 25)

# c) Given the variables: planet = “Earth”, diameter = 12742,
# use .format() to print the following string “The diameter of Earth is 12742 kilometers.”
print("The diameter of {} is {} kilometers.".format("Earth", "12742"))
print("-" * 25)

# d) Given the name list, use indexing to grab word “target”,
# the_list = [1,2,[3,4],[5,[100,200,['target']],23,11],1,7]
the_list = [1, 2, [3, 4], [5, [100, 200, ['target']], 23, 11], 1, 7]
print(the_list[3][1][2])
print("-" * 25)

# e) Given this nest dictionary grab the work “hello”.
# The_dic = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
The_dic = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
print(The_dic['k1'][3]['tricky'][3]['target'][3])
print("-" * 25)


# f) Create a basic function that returns True if the word 'elephant' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def check_word(input_string, word):
    print("Checking for {} in {}".format(word, input_string))
    if word in input_string:
        return True
    else:
        return False


print(check_word("I saw an elephant", "elephant"))
print(check_word("I saw an tiger", "elephant"))
print(check_word("My dog's food is rotten", "dog"))
print(check_word("Doge coin is expensive", "dog"))
print(check_word("Doge coin is expensive", "Doge"))
print("-" * 25)


# g) Create a function that counts the number of times the word "elephant" occurs in a string.
# Again ignore edge cases.
def word_count(word, input_string):
    return input_string.count(word)


print(word_count('elephant', "Count the elephant in the list of elephants"))
print("-" * 25)


# h) Write a function to return one of 3 possible results: "Low speed", "Medium speed", or "Fast speed".
# If your speed is 60 or less, the result is "Low speed".
# If speed is between 61 and 80 inclusive, the result is "Medium speed".
# If speed is 81 or more, the result is "Fast speed".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday,
# your speed can be 5 higher in all cases.
def calculate_speed(speed, is_my_birthday):
    print("Calculating speed limit for: {} and is it my birthday: {}".format(speed, is_my_birthday))
    birthday_limit = 0
    if is_my_birthday:
        birthday_limit = 5
    if speed <= 60 + birthday_limit:
        return "Low speed"
    elif 61 + birthday_limit <= speed <= 80 + birthday_limit:
        return "Medium speed"
    elif speed >= 81 + birthday_limit:
        return "Fast speed"


print(calculate_speed(60, False))
print(calculate_speed(61, True))
print(calculate_speed(61, False))
print(calculate_speed(88, False))
print(calculate_speed(88, True))
print(calculate_speed(80, False))
print(calculate_speed(84, True))

print("-" * 25, "Workshop 10 End", "-" * 25)
